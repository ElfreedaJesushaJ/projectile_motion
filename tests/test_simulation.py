import pytest

from src.simulation import simulate_projectile_motion


def test_simulation_time_points():
    times, x_positions, y_positions = simulate_projectile_motion(
        0, 0, 20, 45, 9.81, 2, 0.5
    )

    assert len(times) == 5


def test_simulation_initial_position():
    times, x_positions, y_positions = simulate_projectile_motion(
        5, 10, 20, 45, 9.81, 2, 0.5
    )

    assert x_positions[0] == pytest.approx(5)
    assert y_positions[0] == pytest.approx(10)


def test_simulation_position():
    times, x_positions, y_positions = simulate_projectile_motion(
        0, 0, 20, 45, 9.81, 2, 0.5
    )

    assert x_positions[2] == pytest.approx(14.1421356237)
    assert y_positions[2] == pytest.approx(9.2371356237)