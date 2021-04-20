fry_pan_on_face = int(input())
tail_shut_balcony_door = int(input())
paws_trampled_sharp_heels = int(input())
mom_threat = int(input())
total_dragon = int(input())
damaged_dragon = []
for i in range(1, total_dragon+1):
    if i%fry_pan_on_face == 0 or i%tail_shut_balcony_door == 0 or i%paws_trampled_sharp_heels == 0 or i%mom_threat == 0 :
        damaged_dragon.append(i)

print(len(damaged_dragon))