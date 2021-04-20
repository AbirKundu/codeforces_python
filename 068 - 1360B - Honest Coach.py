no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    no_of_athletes = int(input())
    athletes_strength = list(map(int, input().split()))
    athletes_strength.sort()
    min_diff = abs(athletes_strength[1] - athletes_strength[0])
    temp = athletes_strength[1]
    for j in range(2, no_of_athletes):
        diff = abs(athletes_strength[j] - temp)
        min_diff = min(min_diff, diff)
        temp = athletes_strength[j]

    print(min_diff)
