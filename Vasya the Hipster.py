red, blue = map(int, input().split())
diff_pair = min(red, blue)
rem_red = red - diff_pair
rem_blue = blue - diff_pair
same_pair = (rem_red // 2) + (rem_blue // 2)
print(f"{diff_pair} {same_pair}")