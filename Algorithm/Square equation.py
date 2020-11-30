import cmath
from typing import List

abc: List[float] = list(input("Enter the a, b, c of the equation ax^2 + bx + c: ").split())

while len(abc) < 3:
    abc.append(float(0))

a: [float] = float(abc[0])
b: [float] = float(abc[1])
c: [float] = float(abc[2])

delta: [float] = b*b - 4*a*c

x1 = (-b - cmath.sqrt(delta))/2*a
x2 = (-b + cmath.sqrt(delta))/2*a

print('The solution are {0} and {1}'.format(x1, x2))
