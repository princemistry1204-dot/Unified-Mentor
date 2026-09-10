import matplotlib.pyplot as plt
import numpy as np

def plot_data(X, y, ax):
    \"\"\"
    Plots the data points on the provided axis.
    \"\"\"
    y = y.flatten()
    X0 = X[y == 0]
    X1 = X[y == 1]
    ax.scatter(X0[:, 0], X0[:, 1], c='r', marker='x', label='Class 0')
    ax.scatter(X1[:, 0], X1[:, 1], c='g', marker='o', label='Class 1')
    ax.legend()
