order = 'J23456789TQKA'
hand = {}
handsort = [[] for i in range(7)]

while True:
    try:
        s = input().split()
        hand[s[0]] = s[1]
    except EOFError:
        break

for i in hand:
    iorg = i

    joke = i.count('J')
    freq = {}
    for j in i:
        if j in freq:
            freq[j] += 1
        else:
            freq[j] = 1
    sortfreq = sorted(freq, key=lambda x: freq[x])
    if sortfreq[-1] != 'J':
        i = i.replace('J', sortfreq[-1])
    else:
        if len(sortfreq) > 1:
            i = i.replace('J', sortfreq[-2])

    if len(set(i)) == 1:
        handsort[6].append(iorg)
    elif len(set(i)) == 2:
        s1 = set(i)
        s2 = ''
        for j in s1:
            s2 += str(i.count(j))
        if ''.join(sorted(s2)) == '14':
            handsort[5].append(iorg)
        else:
            handsort[4].append(iorg)
    elif len(set(i)) == 3:
        s1 = set(i)
        s2 = ''
        for j in s1:
            s2 += str(i.count(j))
        if ''.join(sorted(s2)) == '113':
            handsort[3].append(iorg)
        else:
            handsort[2].append(iorg)
    elif len(set(i)) == 4:
        handsort[1].append(iorg)
    else:
        handsort[0].append(iorg)

for i in handsort:
    i.sort(key=lambda x: [order.index(c) for c in x])

print(handsort)

sum = 0
count = 1
for i in handsort:
    for j in i:
        sum += int(hand[j])*count
        count += 1
print(sum)
