import numpy as np
import matplotlib.pyplot as plt
import sys

def load_mandelbrot(filename):
    with open(filename, 'r') as f:
        data = [list(map(int, line.strip().split(','))) for line in f]
    return np.array(data)

def plot_mandelbrot(data):
    plt.figure(figsize=(15, 15))
    plt.imshow(data, cmap='inferno', extent=[-2, 1, -1, 1])
    plt.colorbar(label='Iterations')
    plt.title("Mandelbrot Set")
    plt.xlabel("Re")
    plt.ylabel("Im")

    output_filename = "mandelbrot_plot.png"
    plt.savefig(output_filename)
    print(f"Plot saved as {output_filename}")
    plt.show()

if __name__ == "__main__":
    filename = "mandelbrot"
    data = load_mandelbrot(filename)
    plot_mandelbrot(data)
