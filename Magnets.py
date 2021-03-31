no_of_magnets = int(input())
previous_left = -1
count = 1
for i in range(no_of_magnets):
    left, right = input().replace("", " ").split()
    if previous_left == right:
        count += 1
    previous_left = left

print(count)
