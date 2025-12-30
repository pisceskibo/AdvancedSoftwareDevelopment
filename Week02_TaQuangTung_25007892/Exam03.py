"""
Nhập vào một chuỗi các ký tự. Hãy tìm đoạn con liên tiếp (substring) dài nhất mà là chuỗi đối xứng (palindrome).
Nếu có nhiều đoạn con đối xứng dài nhất, in ra đoạn xuất hiện sớm nhất.
+ INPUT: một chuỗi ký tự (không có khoảng trắng)
+ OUTPUT: đoạn con đối xứng dài nhất

VD: babad => bab
"""

def is_palindrome(s):
    return s == s[::-1]

def find_substring_palindrome(string_input):
    n = len(string_input)
    longest = ""

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = string_input[i:j]

            if is_palindrome(substring):
                if len(substring) > len(longest):
                    longest = substring

    return longest

string_input = input("Enter string: ")
keyword_palindrome = find_substring_palindrome(string_input)
print(f"Substring of Palidrome is: {keyword_palindrome}")