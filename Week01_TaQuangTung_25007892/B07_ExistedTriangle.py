"""
Viết chương trình nhập 3 số a, b, c lần lượt là độ dài 3 cạnh của 1 tam giác.
Nếu a, b, c hợp lệ thì in ra TRUE và ngược lại.
"""
a = float(input("Enter a = "))
b = float(input("Enter b = "))
c = float(input("Enter c = "))

if a > 0 and b > 0 and c > 0:
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("TRUE")
    else:
        print("FALSE")
else:
    print("FALSE")