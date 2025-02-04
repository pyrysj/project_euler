def fib_to(n):
    fib = [0, 1]
    # because we have the first two
    for i in range(2,n+1):
        fib.append(fib[i-2]+fib[i-1])
    return fib

def fib_to_4m():
    i = 2
    fib = [0,1]
    while fib[i-1]<4*10**6:
        fib.append(fib[i-2]+fib[i-1])
        i+=1
    # bit of a hack here, but my brain was blanking here
    return fib[:-1]

# generates the list
fib_numbers = fib_to_4m()

# list comprehension
fib_numbers_even = [num for num in fib_numbers if not num & 1]
answer = sum(fib_numbers_even)
print(answer)