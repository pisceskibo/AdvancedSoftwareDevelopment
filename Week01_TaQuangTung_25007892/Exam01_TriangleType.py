"""
Nhập 3 cạnh a, b, c của tam giác:
+ Nếu tam giác cân thì in ra chu vi
+ Nếu tam giác vuông thì in ra chiều cao
+ Nếu tam giác thường thì tính diện tích tam giác bằng công thức Herong: S = sqrt(p*(p - a)*(p - b)*(p - c))
+ Nếu không có trường hợp nào thì in ra FALSE
"""
import math

def resolve_triangle_type(a, b, c):
    if (a + b > c and a + c > b and b + c > a):
        if (a == b) or (a == c) or (b == c):
            chu_vi = a + b + c
            return f"Chu vi = {chu_vi}"
        elif (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
            if a**2 + b**2 == c**2:
                chieu_cao = a*b/c
            elif a**2 + c**2 == b**2:
                chieu_cao = a*c/b
            elif b**2 + c**2 == a**2:
                chieu_cao = b*c/a
            return f"Chiều cao = {chieu_cao}"
        else:
            p = (a + b + c) / 2
            dien_tich_herong = math.sqrt(p*(p - a)*(p - b)*(p - c))
            return f"Diện tích = {dien_tich_herong}"
    else:
        return False

a = float(input("Enter a = "))
b = float(input("Enter b = "))
c = float(input("Enter c = "))

if a > 0 and b > 0 and c > 0:
    triangle_type = resolve_triangle_type(a, b, c)
    print(f"Triangle with ({a}, {b}, {c}) is: {triangle_type}")
else:
    print("FALSE")