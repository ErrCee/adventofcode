lenarr = []

while True:
    try:
        s = input().split(': ')[1].split(' | ')
        win = set(s[0].split())
        num = set(s[1].split())
        lenarr.append(len(win.intersection(num)))
    except EOFError:
        break

arr = [1]*len(lenarr)
for i in range(len(arr)):
    for j in range(i+1, i+1+lenarr[i]):
        arr[j] += arr[i]

print(sum(arr))
