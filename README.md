# Projectile Motion Simulator

A Python-based computational physics project that simulates and visualizes projectile motion.

## Overview

This project models the motion of a projectile launched with an initial velocity and angle.

The current version uses the analytical equations of projectile motion to calculate:

- Horizontal velocity
- Vertical velocity
- Horizontal position
- Vertical position
- Projectile trajectory
- Landing point

The simulation also includes an animated visualization of the projectile's motion.

## Project Structure

```text
projectile_motion/
│
├── src/
│   ├── __init__.py
│   ├── physics.py
│   ├── simulation.py
│   └── visualization.py
│
├── tests/
│   ├── test_physics.py
│   └── test_simulation.py
│
├── assets/
│
├── run_simulation.py
├── requirements.txt
└── README.md

## Future Advancements

- Implement numerical integration using the Euler method
- Implement higher-order methods such as Midpoint and Runge-Kutta 4 (RK4)
- Compare numerical solutions with analytical solutions
- Perform numerical error and convergence analysis
- Analyze conservation of mechanical energy
- Add air resistance and drag forces
- Investigate how launch angle affects projectile range
- Determine the optimal launch angle under different physical conditions
- Add interactive controls for initial velocity, launch angle, and gravity