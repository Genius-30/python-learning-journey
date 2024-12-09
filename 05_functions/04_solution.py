import math

def circle_status(r):
  PI = math.pi
  area = 2 * PI * r
  circumference = PI * r ** 2
  return area, circumference

a, c = circle_status(3)
print("Area of circle", a)
print("Circumference of circle", c)