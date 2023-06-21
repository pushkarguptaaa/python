number = 15 # Initialize the variable
while(number>4): # Complete the while loop condition
    print(number, end=" ")
    number-=5 # Increment the variable

# Should print 15 10 5 

for number in range(1,5+1):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")


# Should print:
# odd
# even
# odd
# even
# odd

def even_numbers(n):
    count = 0
    current_number = 0
    while(current_number<=n): # Complete the while loop condition
        if current_number % 2 == 0:
            count+=1 # Increment the appropriate variable
        current_number+=1 # Increment the appropriate variable
    return count
    
print(even_numbers(25))   # Should print 13
print(even_numbers(144))  # Should print 73
print(even_numbers(1000)) # Should print 501
print(even_numbers(0))    # Should print 1

def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(rows): 
        # Complete the inner loop range to control the number of 
        # asterisks per row
        for y in range(x+1): 
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()


rows_asterisks(5)

def divisible(max, divisor):
    count=0 # Initialize an incremental variable
    for x in range(0,max,divisor): # Complete the for loop
        if x % divisor == 0:
            count+=1 # Increment the appropriate variable
    return count

print(divisible(100, 10)) # Should be 10
print(divisible(10, 3)) # Should be 4
print(divisible(144, 17)) # Should be 9

def all_numbers(minimum, maximum):

    return_string = "" # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # numbers up to and including the "maximum" value.
    for x in range(minimum,maximum+1): 

        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.
        return_string+= str(x) + " "

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
    return return_string.strip()


print(all_numbers(2,6))  # Should be 2 3 4 5 6
print(all_numbers(3,10)) # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1,1)) # Should be -1 0 1
print(all_numbers(0,5))  # Should be 0 1 2 3 4 5
print(all_numbers(0,0))  # Should be 0

for x in range(10):
    for y in range(x):
        print(y)