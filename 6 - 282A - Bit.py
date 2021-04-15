no_of_opertion = int(input())
data = 0
for i in range(no_of_opertion):
	operation = input()
	if '++' in operation:
		data += 1
	else:
		data -= 1
		
print(data)