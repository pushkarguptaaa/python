# program to find HCF of Two Numbers
n1, n2 = 36, 60
hcf = 1
def findHcf(n1, n2):
    for n in range(1, min(n1, n2)):
        if n1 % n == 0 and n2 % n == 0:
            hcf = n
    return hcf
print(findHcf(n1, n2))

# Program for LCM Of Two Numbers
n1, n2 = 12, 14
def findLcm(n1, n2):
    for n in range(max(n1, n2), (n1 * n2)+1, n2):
        if n % n1 == 0 and n % n2 == 0:
            lcm = n
            break
    return lcm
print(findLcm(n1, n2))

# Program for Binary To Decimal Conversion
num = 10
def binaryDecimal(num):
    dec = 0
    base = 1
    while num > 0:
        rem = num % 10
        dec += (rem * base)
        num //= 10
        base *= 2
    return dec
print(binaryDecimal(num))
