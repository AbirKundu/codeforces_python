no_of_games = int(input())
win_pattern = input()
count_a = count_d = 0
for win in win_pattern:
    if win == 'A':
        count_a += 1
    else:
        count_d += 1

if count_a > count_d:
    print("Anton")
elif count_d > count_a:
    print("Danik")
else:
    print("Friendship")