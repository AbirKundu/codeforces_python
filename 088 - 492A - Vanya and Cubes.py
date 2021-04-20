no_of_cube = int(input())
i = 1
count = 0
while no_of_cube >= sum(range(1, i+1)):
    count += 1
    no_of_cube -= sum(range(1, i+1))
    i += 1

print(count)
