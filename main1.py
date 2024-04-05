from area import circle_area
from calculator import *

area = circle_area(5)
print("Circle area(radius = 5): ", area)

x, y = 5, 10
print(f"{x} + {y} = {add(x, y)}")
print(f"{x} - {y} = {subtract(x, y)}")
print(f"{x} * {y} = {multiply(x, y)}")
print(f"{x} / {y} = {divide(x, y)}")
