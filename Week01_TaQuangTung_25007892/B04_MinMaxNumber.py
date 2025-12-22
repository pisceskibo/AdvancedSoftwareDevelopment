"""
Viết chương trình nhập 3 số a, b, c từ bàn phím.
In ra số nhỏ nhất và lớn nhất trong 3 số này trên cùng 1 dòng thỏa mãn: 'min max'
"""

def get_min_max_number(a, b, c):
    array = [a, b, c]
    array.sort()

    return f"{array[0]} {array[-1]}"

a = int(input("Enter a is: "))
b = int(input("Enter b is: "))
c = int(input("Enter c is: "))
min_max_value = get_min_max_number(a, b, c)

print(f"(min, max) = ({min_max_value})")