import math
import cmath

a = float(input("Type the value of a: "))
b = float(input("Type the value of b: "))
c = float(input("TYpe the value of c: "))

lol = math.pow(b, 2)
lol1 = lol -4 * a * c

lol2 = cmath.sqrt(lol1)

lol3 = -b + lol2

lol4 = lol3 / 2

# negative value of the square root

lol5 = -b - lol2

lol6 = lol5 / 2

print(f"x = {lol4.real} and x = {lol6.real}")
