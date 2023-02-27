import random
import math

def eqv(a, b, c):
    if math.isclose(a+b, c, rel_tol=eps):
        return True
    else:
        return False

a = float(random.randomrange(1000, 100000))
b = float(random.randomrange(1000, 100000))
c = float(input())
if a>b:
    eps = a * 0.0001
else:
    eps = b * 0.0001

print(eqv(a, b, c))