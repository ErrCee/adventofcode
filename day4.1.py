sum = 0

while True:
    try:
        s = input().split(': ')[1].split(' | ')
        win = set(s[0].split())
        num = set(s[1].split())
        com = win.intersection(num)
        if len(com) > 0:
            sum += 2**(len(com)-1)
    except EOFError:
        break

print(sum)
