import numpy as np 

from .physics import (
    horizontal_position,
    vertical_position
)

def simulate_projectile_motion(x0, y0,v0, theta, g, duration, dt):
    times = np.arange(0, duration + dt, dt) 

    x_positions = []
    y_positions = []

    for t in times:
        x=horizontal_position(x0, v0, theta, t)
        y=vertical_position(y0, v0, theta, g, t)

        x_positions.append(x)
        y_positions.append(y)

    return times, x_positions, y_positions


def simulate_until_landing(x0, y0, v0, theta, g, dt):
    times = []
    x_positions = []
    y_positions = []

    t = 0.0

    while True:
        x = horizontal_position(x0, v0, theta, t)
        y = vertical_position(y0, v0, theta, g, t)

        times.append(t)
        x_positions.append(x)
        y_positions.append(y)

        if t > 0 and y <= 0:
            break

        t += dt

    return times, x_positions, y_positions