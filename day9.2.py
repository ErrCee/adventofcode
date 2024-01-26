sum = 0

while True:
    try:
        s = [list(map(int, input().split()))]
        condt = 0
        while condt != 1:
            temp = []
            for i in range(1, len(s[-1])):
                temp.append(s[-1][i] - s[-1][i-1])
            s.append(temp)
            if temp.count(0) == len(temp):
                condt = 1
        tsum = s[0][0]
        for i in range(1, len(s)):
            tsum += (-1)**i*s[i][0]
        sum += tsum

    except EOFError:
        break

print(sum)
