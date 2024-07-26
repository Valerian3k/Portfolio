import random

w1 = random.random() * (1 - (-1)) + (-1)
w2 = random.random() * (1 - (-1)) + (-1)
w3 = random.random() * (1 - (-1)) + (-1)

x1 = [0,0,1,1]
x2 = [0,1,0,1]
x3 = [1,1,1,1]
d = [0,1,1,1]
b = [0,0,0,0]
y = [0,0,0,0]
sw = [0,0,0,0]
lk = 0
wsUcz = 0.70


for x in range(4):
    sw[x] = x1[x] * w1 + x2[x] * w2 + x3[x] * w3
    if sw[x] >= 0:
        y[x] = 1
    else:
        y[x] = 0
    b[x] = d[x] - y[x]

print("Przed:")
print("\tBłąd 0: ", b[0])
print("\tBłąd 1: ", b[1])
print("\tBłąd 2: ", b[2])
print("\tBłąd 3: ", b[3])

while (b[0] != 0) or (b[1] != 0) or (b[2] != 0) or (b[3] != 0):
    for x in range(4):
        sw[x] = x1[x] * w1 + x2[x] * w2 + x3[x] * w3
        if sw[x] >= 0:
            y = 1
        else:
            y = 0
        b[x] = d[x] - y

        w1 = w1 + (wsUcz * b[x] * x1[x])
        w2 = w2 + (wsUcz * b[x] * x2[x])
        w3 = w3 + (wsUcz * b[x] * x3[x])
    lk += 1

print("\n")
print("Po:")
print("\tBłąd 0: ", b[0])
print("\tBłąd 1: ", b[1])
print("\tBłąd 2: ", b[2])
print("\tBłąd 3: ", b[3])
print("")
print("Liczba kroków: ", lk)





