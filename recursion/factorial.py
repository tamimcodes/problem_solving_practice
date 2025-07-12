# Program for finding factorial using recurtion

def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num-1)

num = 8
print(factorial(num))
