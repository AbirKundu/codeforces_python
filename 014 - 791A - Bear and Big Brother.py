limak, bob = input().split()    #  limak, bob = map(int,input().split()) <<<<<<<<<< instead of 1st 3 lines.
limak = int(limak)
bob = int(bob)
year_count = 0
while True:
    if limak > bob:
        print(year_count)
        break
    else:
        limak = 3 * limak
        bob = 2 * bob
        year_count += 1
