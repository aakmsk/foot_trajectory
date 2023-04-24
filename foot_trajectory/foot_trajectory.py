import numpy as np
from scipy.special import comb
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class FootTrajectoryGenerator:
    def __init__(self, base_frequency, initial_phi):
        self.base_frequency = base_frequency
        self.initial_phi = initial_phi

    def _compute_phi(self, time, frequency_offset):
        return np.mod(self.initial_phi + (self.base_frequency + frequency_offset) * time, 2 * np.pi)

    def compute_trajectory(self, time, **kwargs):
        pass


class SplineFootTrajectoryGenerator(FootTrajectoryGenerator):
    def _compute_trajectory(self, time, frequency_offset, width, height):
        phi = self._compute_phi(time, frequency_offset)
        x = width / 2 * np.cos(phi)
        k = 2 * (phi - np.pi) / np.pi
        y = np.where(
            (k >= 0) & (k < 1),
            height * (-2 * np.power(k, 3) + 3 * np.power(k, 2)),
            np.where(
                (k >= 1) & (k < 2),
                height * (2 * np.power(k, 3) - 9 * np.power(k, 2) + 12 * k - 4),
                0
            )
        )
        return np.vstack([x, y])

    def compute_trajectory(self, time, frequency_offset=0, width=1, height=1):
        return self._compute_trajectory(time, frequency_offset, width, height)


class SineFootTrajectoryGenerator(FootTrajectoryGenerator):
    def _compute_trajectory(self, time, frequency_offset, width, height):
        phi = self._compute_phi(time, frequency_offset)
        x = width / 2 * np.cos(phi)
        y = np.where(
            (phi >= 0) & (phi < np.pi),
            0,
            height * np.sin(phi - np.pi)
        )
        return np.vstack([x, y])

    def compute_trajectory(self, time, frequency_offset=0, width=1, height=1):
        return self._compute_trajectory(time, frequency_offset, width, height)


class BezierFootTrajectoryGenerator(FootTrajectoryGenerator):
    DESIRED_VELOCITY = 10
    SWING_PERIOD = 1
    POINTS_COUNT = 11
    CONTROL_POINTS = np.array([
        [-0.5, 0],
        [-(0.5 + DESIRED_VELOCITY / ((POINTS_COUNT + 1) * SWING_PERIOD) / 340), 0],
        [-0.88, 0.73],
        [-0.88, 0.73],
        [-0.88, 0.73],
        [0, 0.73],
        [0, 0.73],
        [0, 1],
        [0.88,1],
        [0.88, 1],
        [0.5 + DESIRED_VELOCITY / ((POINTS_COUNT + 1) * SWING_PERIOD) / 340, 0],
        [0.5, 0]
    ])
    def _bezier_curve(self, control_points, t, width, height):
        result = np.array([[0., 0.]]).T * np.arange(len(t))
        for i in range(self.POINTS_COUNT + 1):
            result += comb(self.POINTS_COUNT, i, exact=True) * control_points[i:i+1, :].T * np.power(1-t, self.POINTS_COUNT-i) * np.power(t, i)
        result[0] = width * result[0]
        result[1] = height * result[1]
        return result

    def _compute_trajectory(self, time, frequency_offset, width, height):
        phi = self._compute_phi(time, frequency_offset)
        x = width / 2 * np.cos(phi)
        k = 2 * (phi - np.pi) / np.pi
        result = np.where(
            (phi >= 0) & (phi < np.pi),
            np.vstack([x, -0.1 * np.sin(phi)]),
            self._bezier_curve(self.CONTROL_POINTS, (phi - np.pi) / np.pi, width, height)
        )
        return result

    def compute_trajectory(self, time, frequency_offset=0, width=1, height=1):
        return self._compute_trajectory(time, frequency_offset, width, height)


class TrajectoryAnimation:
    def __init__(self, trajectory, save_name, axis_limits=None, cmap="jet", grid=True):
        if axis_limits is None:
            axis_limits = (-0.75, 0.75, -0.25, 1.25)

        self.trajectory = trajectory
        self.axis_limits = axis_limits
        self.cmap = cmap
        self.grid = grid
        self.fig, self.ax = plt.subplots()
        self.ani = animation.FuncAnimation(self.fig,
                                           self.update,
                                           frames=len(self.trajectory[0]),
                                           interval=1,
                                           init_func=self.initial_plot,
                                           blit=True)
        self.ani.save(save_name)

    def initial_plot(self):
        c = np.ones(len(self.trajectory[0])) * 0.4
        self.scat = self.ax.scatter(x=self.trajectory[0],
                                    y=self.trajectory[1],
                                    c=c,
                                    vmin=0, vmax=1,
                                    cmap=self.cmap)
        self.ax.axis(self.axis_limits)
        if self.grid:
            self.ax.grid(linestyle='dotted')
        return self.scat,

    def update(self, i):
        self.scat.set_offsets(np.c_[self.trajectory[0][i], self.trajectory[1][i]])
        self.scat.set_sizes(np.array([200]))
        self.scat.set_array(np.ones(1) * 0.1)

        return self.scat,
