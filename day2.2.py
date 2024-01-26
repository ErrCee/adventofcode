import re

game = []

while True:
    try:
        s = input()
        redm = greenm = bluem = 0
        red = re.findall('.. red',s)
        green = re.findall('.. green',s)
        blue = re.findall('.. blue',s)
        for i in red:
            if int(i[:2]) > redm:
                redm = int(i[:2])
        for i in green:
            if int(i[:2]) > greenm:
                greenm = int(i[:2])
        for i in blue:
            if int(i[:2]) > bluem:
                bluem = int(i[:2])
        game.append(redm*greenm*bluem)
    except EOFError:
        break

print(sum(game))
