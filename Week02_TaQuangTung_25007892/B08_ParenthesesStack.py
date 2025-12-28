""" BÀI 8: KIỂM TRA TÍNH HỢP LỆ CỦA DẤU NGOẶC (VALID PARENTHESES)
Nhập vào một chuỗi chỉ gồm các ký tự ngoặc (), [], {}.
Kiểm tra các dấu ngoặc có được đóng mở đúng quy tắc không?
+ INPUT: các bộ ký tự ngoặc (), [], {}
+ OUTPUT: chuỗi dấu ngoặc có hợp lệ hay không

VD1: {[()]} => Hợp lệ
VD2: {[(])} => Không hợp lệ
"""

def is_valid_parentheses(str_parentheses, mapping_parentheses):
    checking_stack = []

    for char in str_parentheses:
        if char in mapping_parentheses:
            top_element = checking_stack.pop() if checking_stack else "#"

            if mapping_parentheses[char] != top_element:
                return False
        else:
            checking_stack.append(char)

    return True

mapping_parentheses = {")": "(", "}": "{", "]": "["}
str_input = input("Enter parentheses: ")
is_valid = is_valid_parentheses(str_input, mapping_parentheses)
print(f"Parentheses of {str_input} is {is_valid}")