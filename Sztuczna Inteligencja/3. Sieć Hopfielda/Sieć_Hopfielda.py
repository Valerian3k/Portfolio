x = [1, 1, 1, 0, 1, 1, 1, 0,
     0, 0, 1, 0, 1, 0, 0, 1,
     0, 0, 1, 0, 1, 0, 0, 1,
     0, 0, 1, 0, 1, 0, 0, 1,
     0, 0, 1, 0, 1, 0, 0, 1,
     1, 0, 1, 0, 1, 0, 0, 1,
     1, 0, 1, 0, 1, 0, 0, 1,
     1, 1, 1, 0, 1, 1, 1, 0]

u1 = [0, 0, 0, 0, 1, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0]

w = [[0 for j in range(64)] for i in range(64)] #wagi
ex = [0 for i in range(64)] #wyjscie
s = [0 for i in range(64)] #suma

for i in range(64):
    for j in range(64):
        if i != j:
            w[i][j] = (2*x[i] - 1)*(2*x[j] - 1)
        else:
            w[i][j] = 0

for i in range(64):
    for j in range(64):
        s[i] = s[i] + u1[j] * w[i][j]

for i in range(64):
    if s[i] > 0:
        ex[i] = 1
    elif s[i] == 0:
        ex[i] = u1[i]
    else:
        ex[i] = 0

print("Wektor x:")
k = 0
for i in x:
    print(i, " ", end='')
    k += 1
    if (k % 8 == 0) & (k != 0):
        print("")

print("")
print("Wektor u1:")
k = 0
for i in u1:
    print(i, " ", end='')
    k += 1
    if (k % 8 == 0) & (k != 0):
        print("")

print("")
print("Wyjście:")
k = 0
for i in ex:
    print(i, " ", end='')
    k += 1
    if (k % 8 == 0) & (k != 0):
        print("")
