def sumDigit(num, memo):

    l = len(str(num))
    if l == 1:
        return num

    else:
        if num in memo:
            return memo[num]
        num1 = num % (10**(l//2))
        num2 = num // (10**(l//2))
        _sum = sumDigit(num1, memo) + sumDigit(num2, memo)
        memo[num] = _sum
        print(memo)
        return _sum


def superDigit(num, k):
    memo = {}
    # temp = num
    # for _ in range(k-1):
    #     num = int(str(num)+str(temp))
    num = sumDigit(num, memo)
    num = num*k
    while num > 9:
        num = sumDigit(num, memo)

    return num


print(superDigit(4757362, 10000))
