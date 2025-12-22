"""
Viết chương trình nhập vào tên 3 người từ bàn phím.
In ra tên của những người này theo thứ tự tăng dần của từ điển?
"""

name_array = []
for i in range(3):
    name_i = input(f"Enter the name {i + 1} is: ")
    name_array.append(name_i)

name_array.sort()

print("List of sorted name:")
for new_name in name_array:
    print(new_name)