""" BÀI 10: SẮP XẾP DANH SÁCH THEO TẦN SỐ XUẤT HIỆN (SORTING FREQUENCY)
Nhập vào một dãy số và hãy sắp xếp dãy số sao cho:
+ Số nào xuất hiện nhiều lần hơn thì đứng trước
+ Nếu số lần xuất hiện bằng nhau thì số nhỏ hơn đứng trước

VD1: 1, 1, 2, 2, 2, 3 => 2, 2, 2, 1, 1, 3
VD2: 5, 5, 4, 4, 6 => 4, 4, 5, 5, 6
"""

from collections import Counter

def sort_by_frequency(nums):
    counts = Counter(nums)
    nums.sort(key=lambda x: (-counts[x], x))

    final_nums = [str(item) for item in nums]
    return ", ".join(final_nums)

input_str = input("Enter list of numbers (cách nhau bởi dấu phẩy hoặc khoảng trắng): ")
clean_input = input_str.replace(',', ' ')
nums = [int(x) for x in clean_input.split()]

result = sort_by_frequency(nums)
print(f"Sorting numbers by frequency: {result}")