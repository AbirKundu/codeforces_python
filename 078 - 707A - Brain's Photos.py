n, m = map(int, input().split())
flag = False
for i in range(n):
    row = input().split()
    if 'C' in row or 'M' in row or 'Y' in row:
        flag = True

if flag:
    print("#Color")
else:
    print("#Black&White")
