n, k = map(int, input().split())
data = list(map(int, input().split()))
count = 0
for item in data:
    if 5 - item >= k:
        count += 1

print(count//3)
