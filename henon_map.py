import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def henon_map(x, y, z, a=1.4, b=0.3):
    new_x = 1 - a * x**2 + y
    new_y = b * x
    new_z = 0.5 * z
    return new_x, new_y, new_z

def generate_henon_map_trajectory(iterations, initial_values):
    trajectory = np.zeros((iterations, 3))
    x, y, z = initial_values

    for i in range(iterations):
        trajectory[i, :] = [x, y, z]
        x, y, z = henon_map(x, y, z)

    return trajectory

def plot_henon_map(trajectory):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], s=1, c='r', marker='.')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Henon Map')
    plt.show()

iterations = 1000
initial_values = (0.4, 0.3, 0.01)

henon_trajectory = generate_henon_map_trajectory(iterations, initial_values)
plot_henon_map(henon_trajectory)

