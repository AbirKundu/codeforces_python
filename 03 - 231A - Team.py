no_of_problems = int(input())
solvable_problem = 0
for i in range(no_of_problems):
	data = input().count("1")
	if data < 2:
		solvable_problem += 0
	else:
		solvable_problem += 1

print(solvable_problem)
		
	