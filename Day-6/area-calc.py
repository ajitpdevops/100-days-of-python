import math
test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5

def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)
    print(f"You need approx {number_of_cans} ltrs of paint")

paint_calc(height=test_h, width=test_w, cover=coverage)