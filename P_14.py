# Which starting number, under one million, produces the longest chain?
# rules: n → n/2 (n is even)
#        n → 3n + 1 (n is odd)

def make_chain(x):
    n=x
    chain=[x]
    while n!=1:
        if n%2==0:
            n=int(n/2)
            chain.append(n)
        else:
            n=3*n+1
            chain.append(n)
    return chain

#print(make_chain(1))
#print(len(make_chain(13)))

def num_with_longest_chain_under(x):
    length=0
    starting=0
    for i in range(1,x+1):
        if len(make_chain(i))>length:
            length=len(make_chain(i))
            starting=i
    return starting

print(num_with_longest_chain_under(1000000))
