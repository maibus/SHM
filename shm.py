import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from time import sleep, time

dt = 0.001
T = 10
k = 10
g = 9.81
m = 0.3

X = np.zeros([int(T / dt)])
V = np.zeros([int(T / dt)])
A = np.zeros([int(T / dt)])

X[0] = 0
V[0] = 0
A[0] = - m * g
for n in range(1, int(T / dt)):
    X[n] = X[n - 1] + V[n - 1] * dt + 0.5 * A[n - 1] * dt ** 2
    Tens = - k * X[n]
    W = m * g
    F = Tens - W
    A[n] = F / m
    V[n] = V[n-1] + A[n] * dt

figure, axis = plt.subplots(2, 2)
axis[0, 0].scatter(X, A)
axis[0, 0].set_title("S vs A")

axis[1, 0].scatter(X, V, s = 1)
axis[1, 0].set_title("S vs V")

axis[0, 1].scatter(m * A, A)
axis[0, 1].set_title("F vs A")

axis[1, 1].scatter(m * A, X)
axis[1, 1].set_title("F vs S")

plt.show()
