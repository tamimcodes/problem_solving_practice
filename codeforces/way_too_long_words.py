# 71A. Way Too Long Words

testcase = int(input())
while testcase:
    word = input()
    length = len(word)
    if length <= 10:
        print(word)
    else:
        print(word[0]+str(length-2)+word[-1])

    testcase = testcase - 1
