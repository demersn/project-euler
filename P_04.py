# Find the largest palindrome made from the product of two 3-digit numbers


# We start by creating a function that checks if a number is a palindrome
def is_pal(x):
    string = str(x)
    for z in range(len(string)):
        if string[z] != string[-(z+1)]:
            return False
            continue


# We use it for the desired range of numbers
def problem4():
    for x in range(999, 99, -1):
        for y in range(999, 99, -1):
            if is_pal(x*y) is None:
                return(x*y)
                break


print(problem4())

# This version of the code has trouble exiting the palindrome chek in a way
# that is clean and easy for the other function to use.
