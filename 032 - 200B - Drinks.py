no_of_drink = int(input())
data = sum(map(int, input().split()))
print(round((data/(no_of_drink*100))*100, 12))