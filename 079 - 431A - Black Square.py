first, second, third, fourth = map(int, input().split())
data = input()
total_calorie_burned = 0
for element in data:
    element = int(element)
    if element == 1:
        total_calorie_burned += first
    elif element == 2:
        total_calorie_burned += second
    elif element == 3:
        total_calorie_burned += third
    elif element == 4:
        total_calorie_burned += fourth

print(total_calorie_burned)