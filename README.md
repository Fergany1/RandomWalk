# 🌀 Random Walk Visualization

A Python project that generates and visualizes **random walks** using `matplotlib`. Random walks are a fascinating concept in mathematics and data science, often used to model unpredictable paths in physics, finance, and biology. This project demonstrates how to create and plot random walks with customizable steps and points.

---

## ✨ Features

- **Random Walk Generator**: Creates a sequence of random steps in 2D space.
- **Visualization with Matplotlib**:
  - Color gradient to show progression of steps.
  - Highlights start (green) and end (red) points.
- **Interactive Loop**: Keep generating new walks until you choose to stop.
- **Customizable**:
  - Number of points (`num_points`)
  - Step size and direction randomness.

---

## 🧱 Project Structure
RandomWalk/
├─ random_walk.py      # Class to generate random walks
├─ rw_visual.py        # Visualization script using matplotlib
└─ images/             # (Optional) Save plots here

🎨 Visualization Details

Blue gradient: Indicates progression of steps.
Green dot: Starting point (0,0).
Red dot: Ending point.
Axes are hidden for a clean look.
Equal scaling ensures proportional representation.


🧠 How It Works

RandomWalk class:

fill_walk(): Generates all points until num_points is reached.
get_step(): Randomly chooses direction (±1) and distance (0–8).


rw_visual.py:

Creates a RandomWalk instance.
Plots points using matplotlib with color mapping (plt.cm.Blues).
Interactive loop for multiple walks.

👨‍💻 Author
AbdelRahaman Fergany – Student, Cairo (Maadi)
