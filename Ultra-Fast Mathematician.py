x = input()
y = input()
result = []
for i in range(len(x)):
    if x[i] == y[i]:
        result.append('0')
    else:
        result.append('1')

print(''.join(result))