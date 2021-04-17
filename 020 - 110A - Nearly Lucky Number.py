n = input()
lucky_count = 0
for i in n:
    if i == '7' or i == '4':
        lucky_count += 1
if lucky_count == 7 or lucky_count==4:
    print("YES")
else:
    print("NO")