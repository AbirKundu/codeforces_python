no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    data = list(map(int, input().split()))
    data.sort()

    if data[1] == data[2]:
        print("YES")
        print(f"{data[0]} {data[0]} {data[2]}")
    else:
        print("NO")