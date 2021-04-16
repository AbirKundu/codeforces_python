no_of_letter = int(input())
data = input().replace('',' ').split()
temp = ""
count = 0
for stone in data:
    if temp == stone:
        count += 1
    temp = stone
print(count)