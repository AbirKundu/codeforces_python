k_position = int(input().split()[1])
data = input().split()
count = 0
for score in data:
    if int(score) > 0:
        if int(score) >= int(data[k_position-1]):
            count += 1
        
print(count)
    
