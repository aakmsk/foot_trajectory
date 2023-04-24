# Foot Trajectory Library

This library contains different foot trajectory generator classes for quadruped robots. It includes SplineFootTrajectoryGenerator, SineFootTrajectoryGenerator, and BezierFootTrajectoryGenerator.

## Background

The `SplineFootTrajectoryGenerator` class is based on the paper ["Learning Quadrupedal Locomotion over Challenging Terrain"](https://arxiv.org/abs/2010.11251). This generator uses spline interpolation to create smooth foot trajectories.

The `BezierFootTrajectoryGenerator` class is based on the paper ["Leg Trajectory Planning for Quadruped Robots with High-Speed Trot Gait"](https://www.mdpi.com/2076-3417/9/7/1508). This generator uses Bezier curves to generate foot trajectories that are optimized for high-speed trot gait.

## Installation

1. Clone this repository:
```bash
git clone https://github.com/aakmsk/foot_trajectory.git
```

2. Install 
```bash
cd foot_trajectory
pip install -e .
```

## Usage

First, import the desired trajectory generator class:

```python
from foot_trajectory import SplineFootTrajectoryGenerator, SineFootTrajectoryGenerator, BezierFootTrajectoryGenerator
```
Then, create an instance of the generator and use the compute_trajectory method to generate foot trajectories:
```python
spline_gen = SplineFootTrajectoryGenerator()
spline_trajectory = spline_gen.compute_trajectory()

sine_gen = SineFootTrajectoryGenerator()
sine_trajectory = sine_gen.compute_trajectory()

bezier_gen = BezierFootTrajectoryGenerator()
bezier_trajectory = bezier_gen.compute_trajectory()
```
License
This project is licensed under the MIT License - see the LICENSE file for details.
