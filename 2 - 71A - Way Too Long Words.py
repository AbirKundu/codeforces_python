number_of_words = int(input())
for i in range(number_of_words):
	data = input()
	if len(data) > 10:
		print(f"{data[0]}{len(data)-2}{data[-1]}")
	else:
		print(data)