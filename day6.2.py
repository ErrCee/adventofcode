# This is an aberration since the input is too small
# Try Binary Search

time = 56977793
dist = 499221010971440
# time = 71530
# dist = 940200

count = 0
mid = time//2
if mid*2 == time and mid*mid > dist:
    count -= 1
while mid>0:
    if mid*(time-mid) > dist:
        count += 2
        mid -= 1
    else:
        break

print(count)
