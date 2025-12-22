"""
Viết chương trình nhập vào tên và năm sinh của người dùng. In ra tên và tuổi của người đó theo định dạng sau:
'Hello, <name>. You are <age> years old.'

=> In ra 3 dòng với 3 cách khác nhau
+ Toán tử %
+ Phương thức .format()
+ Sử dụng f-strings
"""
from datetime import datetime

your_name = input("Enter your name: ")
your_year = int(input("Enter your age: "))
age = datetime.now().year - your_year

print("Hello, %s. You are %s years old" % (your_name, age))
print("Hello, {}. You are {} years old".format(your_name, age))
print(f"Hello, {your_name}. You are {age} years old")