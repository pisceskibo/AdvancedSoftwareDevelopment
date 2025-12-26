""" BÀI 1: KIỂM TRA HAI CHUỖI CÓ LÀ ĐẢO NGỮ KHÔNG (ANAGRAM)
Nhập vào 2 chuỗi ký tự. Kiểm tra xem chuỗi này có phải là bản sắp xếp lại các ký tự của chuỗi kia không?
+ INPUT: stringA, stringB
+ OUTPUT: stringA và stringB có phải là đảo ngữ của nhau hay không

VD1: listen, silent => Đảo ngữ
VD2: heart, earth => Đảo ngữ
VD3: tung, tngs => Không là đảo ngữ
"""

def check_anagram_string(str_a, str_b):
    # Reformat String
    str_a = str_a.strip().lower()
    str_b = str_b.strip().lower()

    sorted_str_a = sorted(str_a)
    sorted_str_b = sorted(str_b)

    if sorted_str_a == sorted_str_b:
        return True
    else:
        return False

str_a = input("Enter string A: ")
str_b = input("Enter string B: ")

is_anagram_string = check_anagram_string(str_a, str_b)
print(f"=> {str_a} and {str_b} is anagram string: {is_anagram_string}")