import math

c=0.78539816

for i in range(4):
    c-= (math.cos(c)-c)/(-math.sin(c)-1)
    print(c)
