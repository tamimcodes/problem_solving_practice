# 282A. Bit++

n = int(input())
sum = 0

for i in range(n):
    statement = input()
    if '+' in statement:
        sum+=1
    else:
        sum-=1

print(sum)
