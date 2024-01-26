# This is an aberration since the input is too small

time = [56, 97, 77, 93]
dist = [499, 2210, 1097, 1440]
# time = [7,15,30]
# dist = [9,40,200]
pdt = 1

for i in range(len(time)):
    count = 0
    mid = time[i]//2
    if mid*2 == time[i] and mid*mid > dist[i]:
        count -= 1
    while mid>0:
        if mid*(time[i]-mid) > dist[i]:
            print(mid, end=' ')
            count += 2
            mid -= 1
        else:
            break
    print(count)
    pdt *= count

print(pdt)
