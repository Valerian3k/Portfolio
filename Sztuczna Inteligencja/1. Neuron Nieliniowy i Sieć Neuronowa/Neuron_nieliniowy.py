import random
import math

w1 = random.random() * (1 - (-1)) + (-1)
w2 = random.random() * (1 - (-1)) + (-1)
w3 = random.random() * (1 - (-1)) + (-1)

def progowa_unipolarna(x1, x2, x3):
    sw = x1 * w1 + x2 * w2 + x3 * w3
    if sw > 0:
        return 1
    else:
        return 0

def sigmaidalna(x1, x2, x3):
    sw = x1 * w1 + x2 * w2 + x3 *w3
    return 1/(1 + math.exp(-sw))

print(progowa_unipolarna(4, 5, 2))
print(sigmaidalna(4, 5, 2))
