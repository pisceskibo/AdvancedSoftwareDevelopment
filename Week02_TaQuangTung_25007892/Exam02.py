"""
Nhập vào một chuỗi các văn bản. Hãy chuẩn hóa chuỗi bằng cách:
+ Chuyển tất cả về chữ thường
+ Loại bỏ dấu câu: . , ! ? : ;
+ Các từ được tách bởi khoảng trắng
Sau đó tìm từ xuất hiện nhiều nhất. Nếu có nhiều hơn từ có cùng số lần xuất hiện, chọn từ nhỏ hơn theo thứ tự Alphabet.
Format có dạng: <từ> <số lần xuất hiện>

VD:
+ INPUT: "Hello, hello world! world world?"
+ OUTPUT: world 3
+ Chuẩn hóa: hello hello world word word
"""

from collections import Counter

def change_count_format(string_input, prefix_clearing):
    string_input = string_input.strip().lower()

    # Chuẩn hóa chuỗi
    temp_string = ""
    for item in string_input:
        if item in prefix_clearing:
            temp_string += ""
        else:
            temp_string += item

    # Xóa khoảng trắng dư thừa
    temp_array_string = temp_string.split(" ")
    for i in range(len(temp_array_string)):
        temp_array_string[i] = temp_array_string[i].strip()

    # Mảng dữ liệu mới
    array_string = []
    for i in range(len(temp_array_string)):
        if temp_array_string[i] != "":
            array_string.append(temp_array_string[i])

    counts = Counter(array_string)
    array_string.sort(key=lambda x: (-counts[x], x))
    count_value = 0

    try:
        first_value = array_string[0]

        for i in range(len(array_string)):
            if first_value == array_string[i]:
                count_value += 1
            else:
                break

        if first_value == "":
            return "(Trống)"
        else:
            return f"{first_value} {count_value}"
    except Exception:
        return "(Trống)"

prefix_clearing = [".", ",", "!", "?", ":", ";"]
test_string = input("Enter the string: ")
count_format = change_count_format(test_string, prefix_clearing)
print(f"Max frequency of string is: {count_format}")