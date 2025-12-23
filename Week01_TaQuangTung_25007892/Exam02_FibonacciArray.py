"""
Cho dãy số sau:
F(0) = 1, F(1) = 1
F(n) = F(n - 1) + F(n - 2)

Hãy in ra n phần tử đầu tiên trong dãy Fibonacci trên?
"""

def fib_array(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_array(n - 1) + fib_array(n - 2)

number = int(input("Enter number: "))

array_of_fibonacci = []
for i in range(number):
    array_of_fibonacci.append(fib_array(i))

print(f"Array of Fibonacci with n = {number} is: {array_of_fibonacci}")