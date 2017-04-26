names=[]
import string
with open('p022_names.txt','r') as f:
    content = f.read()
    liste=content.split(',')
    #x=f.split(',')
    #names.append(x)
# print(len(liste))
sorted_list=sorted(liste)
# print(sorted_list)
#first=sorted_list[0]
#last=sorted_list[len(liste)-1]
#lettre=first[1]
#print(first)
#print(first[1])
#print(last)
#print(ord('A')-64)
#print(ord('R')-64)
#print(ord('O')-64)
#print(ord('N')-64)
#print(len(first))
#print(ord(first[1])-64)

def sum_of_name(name):
    sum_=0
    for i in range(1,len(name)-1):
        sum_=sum_+(ord(name[i])-64)
        #print(sum_)
    return sum_

#print(sum_of_name(first))

def total_of_scores(liste):
    score=0
    for i in range(len(sorted_list)):
        score=score+(i+1)*sum_of_name(sorted_list[i])
    return score

print total_of_scores(sorted_list)
