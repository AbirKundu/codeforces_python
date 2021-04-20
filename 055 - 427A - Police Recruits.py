no_of_event = int(input())
events = list(map(int, input().split()))
result = untreated_case = 0
for event in events:
    result += event
    if result < 0:
        untreated_case += 1
        result = 0


print(untreated_case)
