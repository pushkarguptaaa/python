# Check if a Number is Positive and Negative in Python
number = 2
print("positive" if number >= 0 else "negative")

# Check Whether a Number is Even or Odd in Python
print("even" if number % 2 == 0 else "odd")

# Find the Sum of the First N Natural Numbers in Python
number = 5
sum = 0
for n in range(number+1):
    sum += n
print(sum)

# Find the Sum of the Numbers in a Given Interval
num1, num2 = 3, 6
sum = 0
for n in range(num1,num2+1):
    sum += n
print(sum)

# Find the Greatest of the Two Numbers
num1, num2 = 3, 6
if num1 > num2:
    print(num1)
else:
    print(num2)

# Find the Greatest of the Three Numbers
num1, num2, num3 = 3, 6, 2
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

# Check Whether a Year is a Leap Year or Not
year = 2000
if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    print("leap year")
else:
    print("Not a leap year")

# Check Whether a Number is a Prime or Not
number = 31
flag = 0
for n in range(2,number):
    if number % n == 0:
        flag = 1
        break
if flag == 1:
    print("Not Prime")
else:
    print("Prime")

# Find the Prime Numbers in a Given Interval
num1, num2 = 1, 20
primes = []
for n in range(num1,num2+1):
    flag = 0
    if n > 1:
        for i in range(2,n):
            if n % i == 0:
                flag = 1
                break
        if flag == 0:
            primes.append(n)
print(primes)

# Find the sum of the Digits of a Number
# number = input("Enter Number: ")
# sum = 0
# for n in number:
#     sum += int(n)
# print(sum)

# Find the Reverse of a Number
number = 2345
reverse = 0
while(number>0):
    rem = number % 10
    reverse = (reverse * 10) + rem
    number = number // 10
print(reverse)

# Check Whether or Not the Number is a Palindrome
number = 1221
temp  = number
reverse = 0
while temp > 0:
    rem = temp % 10
    reverse = (reverse * 10) + rem
    temp = temp // 10
if reverse == number:
    print("Palindrome")
else:
    print("Not a palindrome")

# Check Whether a Given Number is an Armstrong Number or Not
number = 371
temp = number
order = len(str(number))
sum, digit = 0, 0
for n in range(order):
    digit = temp % 10
    temp = temp // 10
    sum += pow(digit, order)
if sum == number:
    print("armstrong")
else:
    print("not")

# Find the Armstrong Numbers in a given Range
n1, n2 = 10, 10000
for n in range(n1, n2+1):
    order = len(str(n))
    sum, digit = 0, 0
    temp = n
    while temp > 0:
        digit = temp % 10
        temp = temp // 10
        sum += pow(digit,order)
    if sum == n:
        print(n, end = ", ")
print()

# Find the Fibonacci Series up to Nth Term
num = 10
num1, num2 = 0, 1
print(num1, num2, end=" ")
for n in range(2, num):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3 , end=" ")
print()

# Factorial of a Number
num = 6
fact = 1
while num > 0:
    fact *= num
    num = num -1
print(fact)

# Program to find Power of a number
num, power = 2, 3
print(pow(num, power))

# Program to find factors of a number
def printDivisors(n):
    for i in range(1,n+1):
        if n % i == 0:
            print(i, end=" ")
    print()

printDivisors(100)

# Program to Finding out the Prime Factors of a Number
num = 21
i = 2
while num != 1:
    if num % i == 0:
        num = num // i
        print(i, end=" ")
    else:
        i = i + 1
print()

# Check Whether or Not the Number is a Strong Number
number = 145
temp = number
sum = 0
f = [0] * 10
f[0] = 1
f[1] = 1
for n in range(2,10):
    f[n] = f[n-1] * n
while temp > 0:
    digit = temp % 10
    temp = temp // 10
    sum += f[digit]
if(sum == number):
    print("Strong no")
else:
    print("not strong")

# Check Whether or Not the Number is a Perfect Number
num = 28
sum = 0
for n in range(1, num):
    if num % n == 0:
        sum += n
if sum == num:
    print("perfect number")
else:
    print("no")

# Check for Perfect Square
from math import sqrt
def isPerfectSquare(num):
    sr = int(sqrt(num))
    return (sr * sr == num)
print(isPerfectSquare(36))

# Check Whether or Not the Number is an Automorphic Number
num = 376
square = pow(num, 2)
len = len(str(num))
mod = pow(10, len)

if square % mod == num:
    print("Automorphic number")
else:
    print("not")

# Checking Whether the Number is Harshad or not
num = 21
temp = num
sum = 0
while num > 0:
    digit = num % 10
    num = num // 10
    sum += digit
if num % sum == 0:
    print("Harshad")
else:
    print("not")

# Program to check Abundant Number
num = 12
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if num < sum:
    print("abundant no")
else:
    print("not")

# Check Whether or Not the Two Numbers  are Friendly Pairs
def friendlyPair(n1, n2):
    s1, s2 = 0, 0
    for n in range(1, n1):
        if n1 % n == 0:
            s1 += n
    for n in range(1, n2):
        if n2 % n == 0:
            s2 += n
    r1 = s1 // n1
    r2 = s2 // n2
    return r1 == r2

print(friendlyPair(6, 28))