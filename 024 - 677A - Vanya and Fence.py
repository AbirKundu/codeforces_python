no_of_friends, fence_height = map(int, input().split())
friends_height = list(input().split())
width = 0
for i in range(no_of_friends):
    if int(friends_height[i]) > fence_height:
        temp = int(friends_height[i]) // fence_height
        if int(friends_height[i]) % fence_height == 0:
            width = width + temp
        else:
            width = width + temp + 1
    else:
        width += 1

print(width)