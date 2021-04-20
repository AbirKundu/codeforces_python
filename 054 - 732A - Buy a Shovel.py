price_of_shovel, coin = map(int, input().split())
i = 1
while True:
    if (price_of_shovel * i) % 10 == coin or (price_of_shovel * i) % 10 == 0:
        print(i)
        break
    else:
        i += 1
