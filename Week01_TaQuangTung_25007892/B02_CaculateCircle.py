"""
Viết chương trình nhập vào số r từ bàn phím.
In ra chu vi và diện tích hình tròn có bán kính r?
"""
import math

def chu_vi_hinh_tron(r):
    return 2 * math.pi * r

def dien_tich_hinh_tron(r):
    return math.pi * r**2

r = float(input("Enter the radius of circle: "))
chu_vi = chu_vi_hinh_tron(r)
dien_tich = dien_tich_hinh_tron(r)

print(f"Chu vi hình tròn với bán kính r = {r} là: {chu_vi}")
print(f"Diện tích hình tròn với bán kính r = {r} là: {dien_tich}")