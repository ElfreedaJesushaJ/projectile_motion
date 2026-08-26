import pytest

from src.physics import (
    horizontal_velocity,
    vertical_velocity,
    horizontal_position,
    vertical_position,
)


def test_horizontal_velocity():
    result = horizontal_velocity(20, 45)

    assert result == pytest.approx(14.1421356237)


def test_vertical_velocity():
    result = vertical_velocity(20, 30, 9.81, 1)

    assert result == pytest.approx(0.19, abs=0.01)


def test_horizontal_position():
    result = horizontal_position(0, 20, 45, 1)

    assert result == pytest.approx(14.1421356237)


def test_vertical_position():
    result = vertical_position(0, 20, 30, 9.81, 1)

    assert result == pytest.approx(5.095)