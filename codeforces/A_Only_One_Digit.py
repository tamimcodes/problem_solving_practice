t = int(input())
for i in range(t):
    n = input()
    if len(n) == 1:
        print(n)
    else:
        print(min(n))