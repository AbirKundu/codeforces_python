no_of_citizen = int(input())
citizen_welfare = list(map(int, input().split()))
max_welfare = max(citizen_welfare)
min_burles = 0
for citizen in citizen_welfare:
    min_burles += (max_welfare - citizen)

print(min_burles)