data = []
for i in range(5):
    data.extend(input().split())

if data.index('1') in [0, 4, 20, 24]:
    print(4)
elif data.index('1') in [7, 11, 13, 17]:
    print(1)
elif data.index('1') in [2, 6, 8, 10, 14, 16, 18, 22]:
    print(2)
elif data.index('1') == 12:
    print(0)
else:
    print(3)