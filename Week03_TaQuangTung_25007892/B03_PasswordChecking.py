""" BÀI 3: MẬT KHẨU HỢP LỆ
Mật khẩu của tài khoản hợp lệ:
+ Độ dài từ 8 đến 100 ký tự
+ Có các chữ cái in HOA và in thường
+ Có số
+ Có ký tự đặc biệt như: ~ ! @ # $ % ^ & *
"""

def checkPassword(s):
    if not (8 <= len(s) <= 100):
        return False

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    special_chars = "~!@#$%^&*"

    for char in s:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    return has_upper and has_lower and has_digit and has_special


if __name__ == "__main__":
    password_input = input("Enter password: ")

    if checkPassword(password_input):
        print("Mật khẩu hợp lệ")
    else:
        print("Mật khẩu không hợp lệ")