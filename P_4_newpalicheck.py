# Find the largest palindrome made from the product of two 3-digit numbers

# We start by creating a function that checks if a number is a palindrome
def is_pal(x):
    string=str(x)
    gnirts=string[::-1]
    if string==gnirts:
        return True
    else:
        return False

# We use it for the desired range of numbers
def problem4():
    max_pali=1
    for x in range(999,99,-1):
        for y in range(999,99,-1):
            if is_pal(x*y) == True and (x*y)>max_pali:
                max_pali=x*y
    return max_pali

print(problem4())
