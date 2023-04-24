# Foot Trajectory Library

This library contains different foot trajectory generator classes for quadruped robots. It includes SplineFootTrajectoryGenerator, SineFootTrajectoryGenerator, and BezierFootTrajectoryGenerator.

## Background

The `SplineFootTrajectoryGenerator` class is based on the paper ["Learning Quadrupedal Locomotion over Challenging Terrain"](https://arxiv.org/abs/2010.11251). This generator uses spline interpolation to create smooth foot trajectories.

The `BezierFootTrajectoryGenerator` class is based on the paper ["Leg Trajectory Planning for Quadruped Robots with High-Speed Trot Gait"](https://www.mdpi.com/2076-3417/9/7/1508). This generator uses Bezier curves to generate foot trajectories that are optimized for high-speed trot gait.

## Installation

1. Clone this repository:
