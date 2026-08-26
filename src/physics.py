import numpy as np


def horizontal_velocity(v0, theta):
    return v0 * np.cos(np.radians(theta))


def vertical_velocity(v0, theta, g, t):
    return v0 * np.sin(np.radians(theta)) - g*t


def horizontal_position(x0, v0, theta, t):
    return x0 + horizontal_velocity(v0, theta) * t


def vertical_position(y0, v0, theta, g, t):
    return y0 + v0 * np.sin(np.radians(theta)) * t - 0.5 * g * t**2