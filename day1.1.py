sum = 0
while(True):
    try:
        lin = ''
        s = input()
        for i in s:
            if i.isdigit():
                lin += i
        sum += int(lin[0]+lin[-1])
    except:
        break

print(sum)
