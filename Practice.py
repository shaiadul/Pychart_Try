#  _____________________________________________reverse a number
n = int(input("Enter a number"))
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
print('Reverse of the number:', rev)

# ------------------------------------Check a Palindrome number
n = int(input("Enter a number"))
temp = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if rev == temp:
    print('The number is a palindrome')
else:
    print("The number isn't a palindrome")

# ---------------------------fibonacci - 0 1 1 2 3 5 8.......
n = int(input("Enter number:"))
a = 0
b = 1
if n < 0:
    print("Incorrect input")
elif n == 0:
    print(a)
elif n == 1:
    print(a)
else:
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    print(b)

# ----------------------------10 is the total number to print
for num in range(6):
    for i in range(num):
        print(num, end=" ")  # print number
    # new line after each row to display pattern correctly
    print("\n")

# --------------------------------------------check even odd
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print(num, " is even")
else:
    print(num, " is odd")

# ----------------------------check positive, negative or 0
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# ----------------------------------Factorial of a number
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)
