"""
Viết chương trình nhập 2 số a và b từ bàn phím.
Tính tổng hai số đó?
"""
def sum_of_numbers(number_a, number_b):
    return number_a + number_b

a = int(input("Number a is: "))
b = int(input("Number b is: "))
sum_value = sum_of_numbers(a, b)

print(f"Sum of ({a}, {b}) is {sum_value}")