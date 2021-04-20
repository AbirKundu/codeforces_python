no_of_teams = int(input())
home_lst = []
away_lst = []
count = 0
for i in range(no_of_teams):
    home, away = list(map(int, input().split()))
    home_lst.append(home)
    away_lst.append(away)

for i in home_lst:
    count += away_lst.count(i)

print(count)