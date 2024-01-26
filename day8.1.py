count = 0
links = {}
direc = input()
l = len(direc)
ignore = input()

while True:
    try:
        s = input()
        links[s[:3]] = [s[7:10], s[12:15]]
    except EOFError:
        break

start = 'AAA'
idx = 0
while start != 'ZZZ':
    if direc[idx] == 'L':
        start = links[start][0]
    else:
        start = links[start][1]
    count += 1
    idx = (idx+1)%l

print(links, count)
