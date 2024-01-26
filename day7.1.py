order = '23456789TJQKA'
hand = {}
handsort = [[] for i in range(7)]

while True:
    try:
        s = input().split()
        hand[s[0]] = s[1]
    except EOFError:
        break

for i in hand:
    if len(set(i)) == 1:
        handsort[6].append(i)
    elif len(set(i)) == 2:
        s1 = set(i)
        s2 = ''
        for j in s1:
            s2 += str(i.count(j))
        if ''.join(sorted(s2)) == '14':
            handsort[5].append(i)
        else:
            handsort[4].append(i)
    elif len(set(i)) == 3:
        s1 = set(i)
        s2 = ''
        for j in s1:
            s2 += str(i.count(j))
        if ''.join(sorted(s2)) == '113':
            handsort[3].append(i)
        else:
            handsort[2].append(i)
    elif len(set(i)) == 4:
        handsort[1].append(i)
    else:
        handsort[0].append(i)

for i in handsort:
    i.sort(key=lambda x: [order.index(c) for c in x])

sum = 0
count = 1
for i in handsort:
    for j in i:
        sum += int(hand[j])*count
        count += 1
print(sum)
