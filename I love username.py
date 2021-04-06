no_of_contest = int(input())
scores = list(map(int, input().split()))
min_value = scores[0]
max_value = scores[0]
count = 0
for i in range(1, no_of_contest):
    if scores[i] > max_value or scores[i] < min_value:
        count += 1
    max_value = max(max_value, scores[i])
    min_value = min(min_value, scores[i])


print(count)
