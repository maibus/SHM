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

figure, axis = plt.subplots(3, 1)
axis[0].scatter(np.linspace(0, T, int(T / dt)), X)
axis[0].set_title("S vs T")

axis[1].scatter(np.linspace(0, T, int(T / dt)), V)
axis[1].set_title("V vs T")

axis[2].scatter(np.linspace(0, T, int(T / dt)), A)
axis[2].set_title("A vs T")

plt.show()
