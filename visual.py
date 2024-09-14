import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the landscape (Mount Everest and its valley)
x = np.linspace(-10, 10, 1000)
y = 5 * np.exp(-0.5 * (x / 2) ** 2)  # Gaussian peak to represent the mountain

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(-10, 10)
ax.set_ylim(-1, 6)
ax.set_aspect('equal')
ax.set_title('Stick Figure Hiking Mount Everest')
ax.set_xlabel('Distance')
ax.set_ylabel('Elevation')

# Plot the landscape
ax.plot(x, y, color='brown')

# Initialize the stick figure components
head_line, = ax.plot([], [], 'k')
body_line, = ax.plot([], [], 'k')
left_arm_line, = ax.plot([], [], 'k')
right_arm_line, = ax.plot([], [], 'k')
left_leg_line, = ax.plot([], [], 'k')
right_leg_line, = ax.plot([], [], 'k')

def get_stick_figure(x0, y0, step):
    """
    Returns the coordinates of the stick figure's body parts.
    """
    # Stick figure dimensions
    body_length = 0.5
    arm_length = 0.3
    leg_length = 0.4
    head_radius = 0.1

    # Head (circle)
    theta = np.linspace(0, 2 * np.pi, 100)
    head_x = x0 + head_radius * np.cos(theta)
    head_y = y0 + head_radius * np.sin(theta)

    # Body (line)
    body_x = [x0, x0]
    body_y = [y0, y0 - body_length]

    # Arms (lines)
    left_arm_x = [x0, x0 - arm_length]
    left_arm_y = [y0 - 0.2, y0 - 0.2 - (0.1 if step else -0.1)]
    right_arm_x = [x0, x0 + arm_length]
    right_arm_y = [y0 - 0.2, y0 - 0.2 - (-0.1 if step else 0.1)]

    # Legs (lines)
    left_leg_x = [x0, x0 - leg_length]
    left_leg_y = [y0 - body_length, y0 - body_length - (leg_length + (0.1 if step else -0.1))]
    right_leg_x = [x0, x0 + leg_length]
    right_leg_y = [y0 - body_length, y0 - body_length - (leg_length + (-0.1 if step else 0.1))]

    return (head_x, head_y, body_x, body_y, left_arm_x, left_arm_y,
            right_arm_x, right_arm_y, left_leg_x, left_leg_y,
            right_leg_x, right_leg_y)

# Path of the stick figure
num_frames = 200
x_path = np.linspace(-9, 9, num_frames)
y_path = 5 * np.exp(-0.5 * (x_path / 2) ** 2)

def init():
    """Initialize the animation."""
    head_line.set_data([], [])
    body_line.set_data([], [])
    left_arm_line.set_data([], [])
    right_arm_line.set_data([], [])
    left_leg_line.set_data([], [])
    right_leg_line.set_data([], [])
    return head_line, body_line, left_arm_line, right_arm_line, left_leg_line, right_leg_line

def animate(i):
    """Animate the stick figure."""
    x0 = x_path[i]
    y0 = y_path[i] + 0.5  # Position stick figure slightly above the ground
    step = (i // 10) % 2 == 0  # Alternate steps every 10 frames

    # Get stick figure coordinates
    (head_x, head_y, body_x, body_y, left_arm_x, left_arm_y,
     right_arm_x, right_arm_y, left_leg_x, left_leg_y,
     right_leg_x, right_leg_y) = get_stick_figure(x0, y0, step)

    # Update lines
    head_line.set_data(head_x, head_y)
    body_line.set_data(body_x, body_y)
    left_arm_line.set_data(left_arm_x, left_arm_y)
    right_arm_line.set_data(right_arm_x, right_arm_y)
    left_leg_line.set_data(left_leg_x, left_leg_y)
    right_leg_line.set_data(right_leg_x, right_leg_y)
    return head_line, body_line, left_arm_line, right_arm_line, left_leg_line, right_leg_line

# Create the animation
anim = FuncAnimation(fig, animate, init_func=init,
                     frames=num_frames, interval=50, blit=True)

# Display the animation
plt.show()

# To save the animation as a video file, uncomment the following line:
# anim.save('stick_figure_hiking.mp4', writer='ffmpeg')
