"""
Viết chương trình nhập vào số nguyên.
Nếu là số nguyên tố thì in ra TRUE và ngược lại
"""

def check_prime_number(number):
    if number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

number = int(input("Enter number: "))

bool_check = check_prime_number(number)

if bool_check:
    print("TRUE")
else:
    print("FALSE")