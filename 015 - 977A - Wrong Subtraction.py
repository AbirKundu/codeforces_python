str_number , times = input().split()
number = int(str_number)
times = int(times)
for i in range(times):
    if str_number[-1] == '0':
        number //= 10
        str_number = str(number)
    else:
        number -=1
        str_number = str(number) 
        
print(str_number)