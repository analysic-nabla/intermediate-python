import numpy as np

def make_training_data(n0, n1, seed=None):
    np.random.seed(123)
    n0, n1 = 200, 200
    x0 = np.random.randn(n0, 2) + np.array([1, 1.5])
    x1 = np.random.randn(n1, 2) + np.array([-1, -1])
    x = np.r_[x0, x1]
    labs = np.r_[np.ones((n0, 1)), np.zeros((n1, 1))]
    colors = []
    colors_map = {0: "tab:blue", 1: "tab:red"}
    for label in labs.ravel(): colors.append(colors_map[label])
    
    return x, labs, colors
