n = int(input())
p_arr = list(map(int, input().split()))
result = [0] * n

for i in range(0, n):
    result[p_arr[i] - 1] = i + 1

print(" ".join(str(elem) for elem in result))
