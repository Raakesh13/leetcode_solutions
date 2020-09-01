"""function to check if ALL the numbers in a given list of integers are PART of the series defined 
by the following. f(0) = 0 f(1) = 1 f(n) = 2*f(n-1) - 2*f(n-2) for all n > 1."""


def is_part_of_series(lst):
    # function to check number is even or odd
    def isEven(number):
        if number % 2 == 0:
            return True
        else:
            return False

    # function to check the whether the number satisfies:{ f(0) = 0 f(1) = 1 f(n) = 2*f(n-1) - 2*f(n-2)}
    def check(number):

        if number == 0 or number == 1:
            return True

        import math
        power = math.log(abs(number), 2)

        if not isEven(power):
            power -= 1

        subpower = power // 2  # get the multiples of 2's in power

        # if multiple of 2's is odd and number < 0 return True
        if not isEven(subpower) and number < 0:
            return True
        # if multiple of 2's is even and number > 0 return True
        elif isEven(subpower) and number > 0:
            return True
        else:
            return False  # if the above conditions are false then return False

    for number in lst:
        if not isEven(number):
            return False
        if not check(number):
            return False

    return True
