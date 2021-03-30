no_of_stops = int(input())
passenger = 0
max_passenger = 0
for i in range(no_of_stops):
    out, inp = input().split()
    out = int(out)
    inp = int(inp)
    passenger = passenger - out + inp
    if max_passenger < passenger:
        max_passenger = passenger

print(max_passenger)