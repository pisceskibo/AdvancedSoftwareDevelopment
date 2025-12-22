"""
Viết chương trình nhập vào 3 số từ bàn phím tương ứng với Ngày, Tháng, Năm.
+ Nếu Ngày, Tháng, Năm không hợp lệ thì in ra FALSE
+ Nếu Ngày, Tháng, Năm hợp lệ thì in ra ngày đó là ngày thứ mấy trong năm

VD: 5 5 2025 => 124 (ngày 5 tháng 5 năm 2025 là ngày thứ 124 trong năm)
"""

# Kiểm tra năm nhuận
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    else:
        return 0

# Nhập liệu giá trị
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

is_valid = True
if year < 1:
    is_valid = False
elif month < 1 or month > 12:
    is_valid = False
elif day < 1 or day > get_days_in_month(month, year):
    is_valid = False

if is_valid:
    sum_of_day_in_year = 0
    for m in range(1, month):
        sum_of_day_in_year += get_days_in_month(m, year)

    sum_of_day_in_year += day

    print(f"Ngày {day} tháng {month} năm {year} là ngày {sum_of_day_in_year - 1} trong năm")
else:
    print("FALSE")