no_of_test_cases = int(input())
for i in range(no_of_test_cases):
    no_of_candies = int(input())
    candies = list(map(int, input().split()))
    if no_of_candies > 1:
        ones = candies.count(1) * 1
        twos = candies.count(2) * 2
        if ones == 0 and no_of_candies % 2 != 0:
            print("NO")
        else:
            diff = abs(twos - ones)
            if diff % 2 == 0:
                print("YES")
            else:
                print("NO")
    else:
        print("NO")