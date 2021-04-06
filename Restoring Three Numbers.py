data = list(map(int, input().split()))
sum_a_b_c = max(data)
data.remove(sum_a_b_c)
one = sum_a_b_c - data[0]
two = sum_a_b_c - data[1]
three = sum_a_b_c - data[2]
print(f"{one} {two} {three}")