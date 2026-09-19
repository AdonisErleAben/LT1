import math

radius = float(input("Enter radius in meters: "))

area = math.pi * math.pow(radius, 2)
Circumference = 2 * math.pi * radius
SquareRoot = math.sqrt(area)
areaRoundedDown = math.floor(area)
areaRoundedUp = math.ceil(area)

print(f"Area of the garden is {area:.2f}")
print(f"Circumference of the garden is {Circumference:.2f}")
print(f"SquareRoot of the garden is {SquareRoot:.2f}")
print(f"Area of the garden rounded down is {areaRoundedDown}")
print(f"Area of the garden rounded up is {areaRoundedUp}")
