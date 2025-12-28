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

    # Sắp xếp danh sách theo thứ tự alphabet
    strs.sort()

    first = strs[0]
    last = strs[-1]
    result = ""

    # Chỉ cần so sánh từ đầu và từ cuối
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            result += first[i]
        else:
            break

    return result


# Chạy thử
print(longest_common_prefix_sorting(["flower", "flow", "flight"]))  # Output: ""