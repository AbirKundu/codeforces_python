no_of_rows = int(input())
pattern = []
flag = True
for i in range(no_of_rows):
    temp = input()
    if "OO|OO" in temp and flag:
        temp = temp.replace("OO|OO", "++|OO")
        flag = False
    elif "OO" in temp and flag:
        temp = temp.replace("OO", "++")
        flag = False
    pattern.append(temp)
if flag:
    print("NO")
else:
    print("YES")
    for ele in pattern:
        print(ele)