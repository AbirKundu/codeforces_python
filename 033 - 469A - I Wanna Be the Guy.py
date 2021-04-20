no_of_level = int(input())
x_level = list(map(int, input().split()))
x_level.pop(0)
y_level = list(map(int, input().split()))
y_level.pop(0)
levels = set(x_level + y_level)
if len(levels) == no_of_level:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
