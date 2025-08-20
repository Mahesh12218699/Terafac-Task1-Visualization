import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Example: generate dummy placements (replace with your actual data)
# Each tuple is (x, y, z, orientation) where orientation = 'X', 'Y', or 'Z'
placements = []
for i in range(5):          # 5 bricks along X
    for j in range(3):      # 3 bricks along Y
        for k in range(2):  # 2 bricks along Z
            if (i+j+k) % 3 == 0:
                orient = 'X'
            elif (i+j+k) % 3 == 1:
                orient = 'Y'
            else:
                orient = 'Z'
            placements.append((i*0.2, j*0.1, k*0.1, orient))

# --- Function to plot 3D bricks ---
def plot_3d_bricks(bricks, limit=None):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Optional limit for speed
    if limit is not None:
        bricks = bricks[:limit]

    for (x, y, z, orient) in bricks:
        # Assign brick dimensions based on orientation
        if orient=='X':
            dx, dy, dz = 0.2, 0.1, 0.1
        elif orient=='Y':
            dx, dy, dz = 0.1, 0.2, 0.1
        else:  # 'Z'
            dx, dy, dz = 0.1, 0.1, 0.2

        # Define corners of the cuboid
        corners = np.array([
            [x, y, z],
            [x+dx, y, z],
            [x+dx, y+dy, z],
            [x, y+dy, z],
            [x, y, z+dz],
            [x+dx, y, z+dz],
            [x+dx, y+dy, z+dz],
            [x, y+dy, z+dz]
        ])

        # Define faces for Poly3DCollection
        faces = [
            [corners[0], corners[1], corners[2], corners[3]],
            [corners[4], corners[5], corners[6], corners[7]],
            [corners[0], corners[1], corners[5], corners[4]],
            [corners[2], corners[3], corners[7], corners[6]],
            [corners[1], corners[2], corners[6], corners[5]],
            [corners[4], corners[7], corners[3], corners[0]]
        ]

        ax.add_collection3d(Poly3DCollection(faces, facecolors='red', edgecolors='k', alpha=0.9))

    ax.set_xlabel("X (m)")
    ax.set_ylabel("Y (m)")
    ax.set_zlabel("Z (m)")
    ax.set_xlim(0, max([b[0]+0.2 for b in bricks]))
    ax.set_ylim(0, max([b[1]+0.2 for b in bricks]))
    ax.set_zlim(0, max([b[2]+0.2 for b in bricks]))
    ax.view_init(20, 30)
    plt.title("3D Visualization of Bricks")
    plt.show()

# --- Call the function ---
plot_3d_bricks(placements, limit=1000)  # you can remove 'limit' if needed
