from src.simulation import simulate_until_landing
from src.visualization import animate_trajectory


times, x_positions, y_positions = simulate_until_landing(
    0, 0, 20, 45, 9.81, 0.02
)

animate_trajectory(x_positions, y_positions)