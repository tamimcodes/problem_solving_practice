# A. Watermelon
# A number can be divided into two even numbers if and only if it is Even and greater than 2

weight = int(input())
if weight <= 2:
    print("NO")
elif weight % 2 == 0:
    print("YES")
else:
    print("NO")
