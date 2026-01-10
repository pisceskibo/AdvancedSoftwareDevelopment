""" BẢI 4: TÍNH PHƯƠNG SAI
Cho danh sách các số thực, hãy tính các giá trị sau:
+ Giá trị trung bình là trung bình cộng của các giá trị có trong danh sách
+ Phương sai tính bằng: delta = 1\n sum(x_i - e)^2 với i = [1, 2, ..., n]
+ Độ lệch chuẩn tính bằng căn bậc hai của phương sai
"""

# Tìm giá trị trung bình
import math

def mean(s):
    if len(s) == 0:
        return 0

    return sum(s) / len(s)

# Tìm phương sai
def variance(s):
    if len(s) == 0:
        return 0

    sum_of_distance_variance = 0
    for x in s:
        sum_of_distance_variance += (x - mean(s))**2

    return sum_of_distance_variance / len(s)

# Tìm độ lệch chuẩn
def standarddeviattion(s):
    return math.sqrt(variance(s))


if __name__ == "__main__":
    n = int(input("Enter length of array: "))
    data_array = []
    for i in range(n):
        item = float(input(f"Item{i} is: "))
        data_array.append(item)

    print(f"Danh sách: {data_array}")
    print(f"1. Trung bình: {mean(data_array)}")
    print(f"2. Phương sai: {variance(data_array)}")
    print(f"3. Độ lệch chuẩn: {standarddeviattion(data_array)}")