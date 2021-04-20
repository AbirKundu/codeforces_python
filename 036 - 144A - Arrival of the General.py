no_of_soldiers = int(input())
heights = list(map(int, input().split()))
temp = heights[0]
max_extra = min_extra = count = 0
start = -1
loc = 0
while True:
    try:
        loc = heights.index(min(heights), start+1)
    except ValueError:
        break
    else:
        start = loc
for i in range(loc, no_of_soldiers):
    if temp < heights[i]:
        heights[i - 1] = heights[i]
        heights[i] = temp
        count += 1
    temp = heights[i]

if heights[-1] != min(heights):
    min_extra = len(heights) - heights.index(min(heights)) - 1
if heights[0] != max(heights):
    max_extra = heights.index(max(heights))
print(count + min_extra + max_extra)
