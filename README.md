# Foot Trajectory Library

This library contains different foot trajectory generator classes for quadruped robots. It includes SplineFootTrajectoryGenerator, SineFootTrajectoryGenerator, and BezierFootTrajectoryGenerator.

## Background

The `SplineFootTrajectoryGenerator` class is based on the paper ["Learning Quadrupedal Locomotion over Challenging Terrain"](https://arxiv.org/abs/2010.11251). This generator uses spline interpolation to create smooth foot trajectories.

The `BezierFootTrajectoryGenerator` class is based on the paper ["Leg Trajectory Planning for Quadruped Robots with High-Speed Trot Gait"](https://www.mdpi.com/2076-3417/9/7/1508). This generator uses Bezier curves to generate foot trajectories that are optimized for high-speed trot gait.

## Supported Trajectories
1. Spline Trajectory
2. Sine Trajectory
3. Bezier Trajectory

## Installation 
```bash
pip install git+https://github.com/aakmsk/foot_trajectory.git
```

## Usage

First, import the desired trajectory generator class:

```python
import numpy as np
from foot_trajectory.foot_trajectory import (
    SplineFootTrajectoryGenerator, 
    SineFootTrajectoryGenerator, 
    BezierFootTrajectoryGenerator,
    TrajectoryAnimation
)
```

Then, create an instance of the generator and use the compute_trajectory method to generate foot trajectories:

```python
spline_generator = SplineFootTrajectoryGenerator(base_frequency=1.0, initial_phi=0.0)
sine_generator = SineFootTrajectoryGenerator(base_frequency=1.0, initial_phi=0.0)
bezier_generator = BezierFootTrajectoryGenerator(base_frequency=1.0, initial_phi=0.0)

t = np.linspace(0, 2 * np.pi, 100)

spline_trajectory = spline_generator.compute_trajectory(t, frequency_offset=0, width=1, height=1)
sine_trajectory = sine_generator.compute_trajectory(t, frequency_offset=0, width=1, height=1)
bezier_trajectory = bezier_generator.compute_trajectory(t, frequency_offset=0, width=1, height=1)  
```
This is a method of saving the trajectory of a movement as an animation.
```python
animation = TrajectoryAnimation(spline_trajectory, save_name="spline_trajectory.gif")
```
License
This project is licensed under the MIT License - see the LICENSE file for details.
