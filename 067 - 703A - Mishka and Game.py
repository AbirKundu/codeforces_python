no_of_games = int(input())
mishka_win_count = chris_win_count = 0
for i in range(no_of_games):
    mishka, chris = map(int, input().split())
    if mishka > chris:
        mishka_win_count += 1
    elif chris > mishka:
        chris_win_count += 1
if mishka_win_count > chris_win_count:
    print("Mishka")
elif chris_win_count > mishka_win_count:
    print("Chris")
else:
    print("Friendship is magic!^^")
