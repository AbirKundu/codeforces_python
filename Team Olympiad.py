no_of_student = int(input())
students = list(map(int, input().split()))
teams = min(students.count(1), students.count(2), students.count(3))
print(teams)
first = second = third = 0
for i in range(teams):
    print(f"{students.index(1, first) + 1} {students.index(2, second) + 1} {students.index(3, third) + 1}")
    first = students.index(1, first) + 1
    second = students.index(2, second) + 1
    third = students.index(3, third) + 1
