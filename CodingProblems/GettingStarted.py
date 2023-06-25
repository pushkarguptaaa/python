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

num = 10
n1, n2 = 0, 1
print("Fibonacci Series:", n1, n2, end=" ")
for i in range(2, num):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3, end=" ")

print()