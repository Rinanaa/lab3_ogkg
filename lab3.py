import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import ConvexHull

file_path = "DS1.txt"

points = []
with open(file_path, "r") as file:
    for line in file:
        x, y = map(int, line.strip().split())
        points.append((x, y))

points = np.array(points)

hull = ConvexHull(points)

canvas_width = 960
canvas_height = 540
dpi = 72

plt.figure(figsize=(canvas_width / dpi, canvas_height / dpi), dpi=dpi)

plt.scatter(points[:, 0], points[:, 1], c="red", s=5, label="Точки")

for simplex in hull.simplices:
    plt.plot(points[simplex, 0], points[simplex, 1], "b-", label="Опукла оболонка" if simplex[0] == hull.simplices[0][0] else "")

plt.axis("off")

output_file = "convex_hull.png"
plt.savefig(output_file)
