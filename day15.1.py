sum = 0

while True:
    try:
        s = input().split(',')
        for i in s:
            cur = 0
            for j in i:
                cur += ord(j)
                cur *= 17
                cur %= 256
            sum += cur
    except EOFError:
        break

print(sum)
