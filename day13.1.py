import numpy as np

rows = 0
cols = 0
proc = []

def processr(arr):
    mir = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            mir = i
    i = mir
    j = mir-1
    while i<len(arr) and j>0:
        if arr[i] == arr[j]:
            pass
        else:
            return processc(arr)
        i += 1
        j -= 1

def processc(arr):
    arr2 = []
    for i in arr:
        arr2.append(list(i))
    arr2 = list(np.array(arr2).transpose())

    mir = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            mir = i
    i = mir
    j = mir-1
    while i<len(arr) and j>0:
        if arr[i] == arr[j]:
            pass
        else:
            processc(arr)
        i += 1
        j -= 1
    cols += mir

while True:
    try:
        s = input()
        if s == '':
            processr(proc)
            proc = []
        else:
            proc.append(s)
    except EOFError:
        break

print(rows*100+cols)
