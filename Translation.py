source = input()
translation = input()
if source[::-1] == translation:
    print("YES")
else:
    print("NO")