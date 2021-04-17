no_of_students, time =input().split()
time = int(time)
queue=list(input())

while (time>0):
	i=0
	while i<(len(queue)-1):
		if (queue[i]=='B' and queue[i+1]=='G'):
			queue[i],queue[i+1]=queue[i+1],queue[i]
			i+=1
		i+=1
	time-=1

print(''.join(queue))