import math

def calculate_hexagon_area(side_length):
    area = (3 * math.sqrt(3) / 2) * (side_length ** 2)
    return area

print("calculate area of a hexagon")
print("enter the side length of the hexagon")
side_length = int(input())
hexagon_area = calculate_hexagon_area(side_length)

print(f"The area of a hexagon with side length {side_length} is: {hexagon_area}")
