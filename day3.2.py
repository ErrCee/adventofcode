sum = 0
arr = []

while True:
    try:
        s = input()
        arr.append(list(s))
    except EOFError:
        break

def isvalid(x, y, arr):
    if x>=0 and y>=0 and x<len(arr) and y<len(arr[0]):
        return True
    else:
        return False

nums = []
directions = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == '*':
            temp = set()
            for k in directions:
                if isvalid(i+k[0], j+k[1], arr) and arr[i+k[0]][j+k[1]].isdigit():
                    s = j+k[1]-1
                    e = j+k[1]+1
                    d = arr[i+k[0]][j+k[1]]
                    while s>=0 and arr[i+k[0]][s].isdigit():
                        d = arr[i+k[0]][s] + d
                        s -= 1
                    while e<len(arr[0]) and arr[i+k[0]][e].isdigit():
                        d += arr[i+k[0]][e]
                        e += 1
                    temp.add(d)
            if len(temp) == 2:
                for l in temp:
                    nums.append(l)

for i in range(0, len(nums), 2):
    sum += int(nums[i])*int(nums[i+1])
print(sum)
