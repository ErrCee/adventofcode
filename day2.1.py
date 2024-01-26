import re

sum = 0
game = []

while True:
    try:
        s = input()
        game.append(1)
        red = re.findall('.. red',s)
        green = re.findall('.. green',s)
        blue = re.findall('.. blue',s)
        for i in red:
            if int(i[:2]) > 12:
                game[-1] = 0
        for i in green:
            if int(i[:2]) > 13:
                game[-1] = 0
        for i in blue:
            if int(i[:2]) > 14:
                game[-1] = 0
    except EOFError:
        break

for i in range(len(game)):
    if game[i] == 1:
        sum += (i+1)
print(sum)
