""" BÀI 5: GÓC GIỮA HAI VECTOR
Tìm góc giữa 2 vector u và v theo công thức: cos(u, v) = (u, v)/|u||v|
"""
import math

def cosineb2v(u, v):
    tich_vo_huong = sum(ui*vi for ui, vi in zip(u, v))

    u_distance = math.sqrt(sum(ui**2 for ui in u))
    v_distance = math.sqrt(sum(vi ** 2 for vi in v))
    if u_distance == 0 or v_distance == 0:
        return 0

    cos_theta = tich_vo_huong/(u_distance * v_distance)
    return cos_theta


if __name__ == "__main__":
    n = int(input("Enter length of array: "))

    # Vector u and v
    u_array = []
    for i in range(n):
        item = float(input(f"Index{i} of u is: "))
        u_array.append(item)

    v_array = []
    for i in range(n):
        item = float(input(f"Index{i} of u is: "))
        v_array.append(item)

    # Cosine(u, v)
    result = cosineb2v(u_array, v_array)
    print(f"cos(u, v) = {result}")