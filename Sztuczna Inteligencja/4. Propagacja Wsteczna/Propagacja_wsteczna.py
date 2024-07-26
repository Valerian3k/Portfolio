import random
import math

learn_ratio = 0.7
m = 0
e = 100000
es = e
u = [0 for j in range(3)]
v = [0 for j in range(3)]
f = [0 for j in range(3)]

x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
x3 = [1, 1, 1, 1]
d = [0, 1, 1, 0]

weight = [[0 for j in range(3)] for i in range(3)]
dw = [[0 for j in range(3)] for i in range(3)]
sdw = [[0 for j in range(3)] for i in range(3)]
for i in range(3): #losowanie wag
    for j in range(3):
        weight[i][j] = random.random() * (1 - (-1)) + (-1)


def activationFunction(x): # funkcja aktywacji
    return 1 / (1 + math.exp(-x))


def activationFunctionDerivative(x):  #pochodna
    return x * (1 - x)


print(f"Ilość kroków: {e}\n")

while e != 0:
    for i in range(4):
        u[0] = x1[i] * weight[0][0] + x2[i] * weight[0][1] + x3[i] * weight[0][2]
        u[1] = x1[i] * weight[1][0] + x2[i] * weight[1][1] + x3[i] * weight[1][2]

        v[0] = activationFunction(u[0])
        v[1] = activationFunction(u[1])

        u[2] = v[0] * weight[2][0] + v[1] * weight[2][1] + x3[i] * weight[2][2]
        v[2] = activationFunction(u[2])     #y

        f[2] = (d[i] - v[2]) * activationFunctionDerivative(v[2])

        f[0] = f[2] * weight[2][0] * activationFunctionDerivative(v[0])
        f[1] = f[2] * weight[2][1] * activationFunctionDerivative(v[1])
        dw[0][0] = learn_ratio * f[0] * x1[i]
        dw[0][1] = learn_ratio * f[0] * x2[i]
        dw[0][2] = learn_ratio * f[0] * x3[i]
        dw[1][0] = learn_ratio * f[1] * x1[i]
        dw[1][1] = learn_ratio * f[1] * x2[i]
        dw[1][2] = learn_ratio * f[1] * x3[i]
        dw[2][0] = learn_ratio * f[2] * x1[i]
        dw[2][1] = learn_ratio * f[2] * x2[i]
        dw[2][2] = learn_ratio * f[2] * x3[i]

        weight[0][0] = weight[0][0] + dw[0][0] + m * sdw[0][0]
        weight[0][1] = weight[0][1] + dw[0][1] + m * sdw[0][1]
        weight[0][2] = weight[0][2] + dw[0][2] + m * sdw[0][2]
        weight[1][0] = weight[1][0] + dw[1][0] + m * sdw[1][0]
        weight[1][1] = weight[1][1] + dw[1][1] + m * sdw[1][1]
        weight[1][2] = weight[1][2] + dw[1][2] + m * sdw[1][2]
        weight[2][0] = weight[2][0] + dw[2][0] + m * sdw[2][0]
        weight[2][1] = weight[2][1] + dw[2][1] + m * sdw[2][1]
        weight[2][2] = weight[2][2] + dw[2][2] + m * sdw[2][2]

        sdw[0][0] = dw[0][0]
        sdw[0][1] = dw[0][1]
        sdw[0][2] = dw[0][2]
        sdw[1][0] = dw[1][0]
        sdw[1][1] = dw[1][1]
        sdw[1][2] = dw[1][2]
        sdw[2][0] = dw[2][0]
        sdw[2][1] = dw[2][1]
        sdw[2][2] = dw[2][2]

        if e == es:
            print(f"Wyjście oczekiwane: {d[i]} \t Wyjście obliczone: {v[2]}")
        if e == 1:
            print(f"Wyjście oczekiwane: {d[i]} \t Wyjście obliczone: {v[2]}")

    e = e - 1
