# Find the sum of all the multiples of 3 or 5 below 1000
def sum_of_multiple(x, y, z):
    # finds the sum of multiples of numbers x and y from 1 to below z
    addi = 0
#    one_to_z=range(z-1)
    for i in range(z):
        if i % x == 0 or i % y == 0:
            addi = addi+i
    return addi


three_and_five = sum_of_multiple(3, 5, 1000)
print(three_and_five)
