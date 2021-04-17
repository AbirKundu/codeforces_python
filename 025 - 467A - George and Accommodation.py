no_of_rooms = int(input())
count = 0
for i in range(no_of_rooms):
    occupied, available = input().split()
    occupied = int(occupied)
    available = int(available)
    if available-occupied >= 2:
        count +=1

print(count)