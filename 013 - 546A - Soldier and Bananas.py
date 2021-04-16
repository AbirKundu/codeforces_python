cost_of_first_banana, dollar, bananas = input().split()
total_dollar = 0
for i in range(1,int(bananas)+1):
	total_dollar += i * int(cost_of_first_banana)

if total_dollar > int(dollar):
    print(total_dollar - int(dollar))
else:
    print(0)
