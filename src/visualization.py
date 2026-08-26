import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate_trajectory(x_positions, y_positions):
    fig, ax = plt.subplots()

    ax.set_xlabel("Horizontal position (m)")
    ax.set_ylabel("Vertical position (m)")
    ax.set_title("Projectile Motion")

    ax.set_xlim(min(x_positions), max(x_positions))
    ax.set_ylim(min(y_positions), max(y_positions))

    ax.grid(True)

    trajectory, = ax.plot([], [])
    projectile, = ax.plot([], [], "o")

    def update(frame):
        trajectory.set_data(
            x_positions[:frame + 1],
            y_positions[:frame + 1]
        )

        projectile.set_data(
            [x_positions[frame]],
            [y_positions[frame]]
        )

        return trajectory, projectile

    animation = FuncAnimation(
        fig,
        update,
        frames=len(x_positions),
        interval=30,
        repeat=False
    )

    plt.show()