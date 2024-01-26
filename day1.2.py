import re

values = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
sum = 0

while(True):
    try:
        s = input()
        lint = {}
        lin = ''
        for i in values:
            if i in s:
                # lint[s.find(i)] = values[i]
                arr = [x.start() for x in re.finditer(i, s)]
                for j in arr:
                    lint[j] = values[i]
        for i in range(len(s)):
            if s[i].isdigit():
                lin += s[i]
            elif i in lint:
                lin += str(lint[i])
        print(lint, lin,end=' ')
        print(lin[0]+lin[-1])
        sum += int(lin[0]+lin[-1])
    except EOFError:
        break

print(sum)
