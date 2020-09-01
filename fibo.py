def fibo(n):
    memo = {0: 0, 1: 1}
    if n in memo:
        return memo[n]
    else:
        f = fibo(n-2)+fibo(n-1)
        memo[n] = f

    return f


print(fibo(0))
print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(4))
print(fibo(5))
