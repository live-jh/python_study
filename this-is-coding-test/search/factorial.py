def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def factorial_recursive(n):
    result =1
    return n


print("반복문을 활용한 입력한 숫자까지의 곱의 합", factorial_iterative(5))
# print("반복문을 활용한 입력한 숫자까지의 곱의 합", factorial_recursive(5))
