""" BÀI 3: KIỂM TRA SỐ HOÀN HẢO (PERFECT NUMBER)
Nhập vào số nguyên dương n. Kiểm tra xem có phải số hoàn hảo không?
(số hoàn hảo có tổng các ước bằng chính nó)
+ INPUT: số nguyên dương n
+ OUTPUT: kiểm tra n có phải số hoàn hảo hay không

VD1: n = 28 => 28 = 1 + 2 + 4 + 7 + 14 => Là số hoàn hảo
"""

def check_is_perfect_number(n):
    if n <= 1:
        return False

    sum_of_number = 0
    for i in range(1, n):
        if n % i == 0:
            sum_of_number += i

    if sum_of_number == n:
        return True
    else:
        return False

number = int(input("Enter number: "))
if check_is_perfect_number(number):
    print(f"{number} is perfect number")
else:
    print(f"{number} is not perfect number")