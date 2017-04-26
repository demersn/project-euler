# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
def fibonacci(n):
    fib_seq=[1,1]
    while len(str(fib_seq[-1])) < n:
        fib_seq.append(fib_seq[-2]+fib_seq[-1])

    return len(fib_seq)

print(fibonacci(100))
