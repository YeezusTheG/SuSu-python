import math

def szamtani_kozep(X):
    i = sum(X) / len(X)
    return i

def mertani_kozep(X):
    multipy_values = 1
    n = len(X)
    for i in X:
        multipy_values = multipy_values * i
    geometric_mean = (multipy_values) ** (1/n)
    return geometric_mean

def negyzetes_kozep(numbers: list) -> float:
    sum_of_squares = sum(x * x for x in numbers)
    return sum_of_squares / len(numbers)

def harmonikus_kozep(numbers: list) ->float:
    reciprocal_sum = sum(1/x for x in numbers)
    return len(numbers) / reciprocal_sum

def modusz(numbers: list) -> float:
    count = {}
    for i in numbers:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    mode = max(count, key=count.get)
    return mode

def median(numbers: list) -> float:
    numbers.sort()
    if len(numbers) % 2 == 0:
        return (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
    else:
        return numbers[len(numbers) // 2]
