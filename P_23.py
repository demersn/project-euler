# Find the sum of all the positive integers which cannot be written
# as the sum of two abundant numbers
import string


# From P_3
def is_factor(x, y):
    if x % y == 0:
        return True
    else:
        return False

# Not needed
# def is_perfect(n):
#     sum_=0
#     for div in range(1,n):
#         if is_factor(n,div)==True:
#             sum_=sum_+div
#             #print(sum_)
#     if n==sum_:     # perfect number
#         return True
#     else:
#         return False


def is_abundant(n):
    sum_ = 0
    for div in range(1, n):
        if is_factor(n, div) is True:
            sum_ = sum_+div
            # print(sum_)
    if sum_ >= n:     # abundant number
        return True
    else:
        return False


# # Generate and store a list of abundant numbers. Do once
# f=open('P_23_stored_abundant.txt','w')
# list_of_abundant=[]
# for i in range(28124):
#     if is_abundant(i)==True:
#         list_of_abundant.append(i)
#         f.write(str(i)+'\n')
# #print(list_of_abundant)
# f.close()
# # And the continue with the rest of the program


# Do the same thing for generating the second list of sum of abundant

with open('P_23_stored_abundant.txt', 'r') as f:
    liste = f.read().splitlines()
f = open('P_23_stored_sumof_abundant.txt', 'w')
list_of_sumof_abundant = []
for a in range(len(liste)):
    for b in range((a), len(liste)):
        # sum_=liste[a]+liste[b]
        f.write(str(int(liste[a])+int(liste[b])) + '\n')
f.close()
# and put it back in comment after


# # Again, creating a file of all numbers under 28123
# f=open('P_23_non_abundant.txt','w')
# l1=[]
# for i in range(283+1):
#     f.write(str(i) +'\n')
# f.close()
# # And close again

# # Then, remove the one that are sum
# import string
# with open('P_23_non_abundant.txt','r') as f:
#     l1=f.read().splitlines()
# with open('P_23_stored_sumof_abundant.txt','r') as g:
#     l2=g.read().splitlines()
# l3 = [x for x in l1 if x not in l2]
# print(l3)


# From P_16
def sum_of_string(string):
    sum_ = 0
    for i in range(len(string)):
        sum_ = sum_+int(string[i])
    return sum_

# print(sum_of_string(l3))
