values = [2, 5, 7, 10, 12, 15, 18, 21, 4, 9, 14]

count_gt_10 = 0
sum_even = 0
between_5_15 = []

for v in values:
    if v > 10:
        count_gt_10 += 1
    if v % 2 == 0:
        sum_even += v
    if 5 <= v <= 15:
        between_5_15.append(v)

print("count_gt_10:", count_gt_10)
print("sum_even:", sum_even)
