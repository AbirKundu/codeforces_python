no_of_problem , time_to_go_party = map(int, input().split())
rem_time = 240 - time_to_go_party
count = 0
time_taken = 0
for i in range(1, no_of_problem+1):
    time_taken += i * 5
    if time_taken <= rem_time:
        count +=1

print(count)