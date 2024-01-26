count = 0
links = {}
direc = input()
l = len(direc)
ignore = input()
start = []

while True:
    try:
        s = input()
        links[s[:3]] = [s[7:10], s[12:15]]
        if s[2] == 'A':
            start.append(s[:3])
    except EOFError:
        break

idx = 0
brk = 0
while brk != 1:
    if direc[idx] == 'L':
        for i in range(len(start)):
            start[i] = links[start[i]][0]
    else:
        for i in range(len(start)):
            start[i] = links[start[i]][1]
    print(start, count)
    count += 1
    idx = (idx+1)%l

    allz = 0
    for i in start:
        if i[-1] == 'Z':
            allz += 1
    if allz == len(start):
        brk = 1

print(count)
