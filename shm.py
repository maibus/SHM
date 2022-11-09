import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
from time import sleep, time


def simulate(m, k, T, dt, g):

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

    return X


def period(arr, leng, mpoint):
    pos = []
    count = 0
    for n in range(1, leng):
        if (arr[n-1] - mpoint) * (arr[n] - mpoint) < 0:
            pos.append(n)
            count += 1
    pos = np.array(pos)
    diff = pos[1:] - pos[:-1]
    return 2 * dt * np.mean(diff)


dt = 0.001
T = 100
g = 9.81

periods = np.zeros(50)
k = np.arange(50)

for i in range(50):
    print(i)
    periods[i] = period(simulate(0.3, k[i], T, dt, g), int(T / dt), (-g * 0.3) / k[i])

plt.scatter(1 / np.sqrt(k), periods)
plt.show()
