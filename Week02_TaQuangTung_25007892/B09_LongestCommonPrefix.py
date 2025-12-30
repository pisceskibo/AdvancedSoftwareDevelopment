""" BÀI 9: TIỀN TỐ CHUNG DÀI NHẤT (LONGEST COMMON PREFIX
Nhập vào một danh sách các từ. Tìm chuỗi các ký tự là tiền tố (phần đầu) chung dài nhất mà tất cả các từ đều có.
+ INPUT: danh sách các từ
+ OUTPUT: chuỗi ký tự tiền tố dài nhất mà các từ đều có

VD1: flower, flow, flight => fl
VD2: dog, racecar, car => None
"""

def longest_common_prefix_sorting(strs):
    if not strs:
        return ""

    # Sort by alphabet
    strs.sort()

    first = strs[0]
    last = strs[-1]
    result = ""

    # Phần tử khác nhau nhất chỉ có ở đầu hoặc ở cuối
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            result += first[i]
        else:
            break

    return result

string_input = input("Enter array of string with space: ")
string_array_input = string_input.strip().split(" ")

array_input = []
for item in string_array_input:
    item = item.strip()
    if item != "":
        array_input.append(item)

print(f"Longest common prefix is: {longest_common_prefix_sorting(array_input)}")