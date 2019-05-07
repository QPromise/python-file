def fibonacci(n, fib = [0, 1]):
    if n >= len(fib):
        for i in range(len(fib), n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]

n = int(input('求幾個費式數？'))
for i in range(0, n):
    print(fibonacci(i), end=' ')