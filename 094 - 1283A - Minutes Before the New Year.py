no_of_test_cases = int(input())
total_mins = 24 * 60
for i in range(no_of_test_cases):
    hours, min = map(int, input().split())
    mins = total_mins - (hours*60 + min)
    print(mins)