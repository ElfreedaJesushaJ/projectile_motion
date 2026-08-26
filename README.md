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
