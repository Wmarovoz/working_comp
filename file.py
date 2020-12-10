#!/usr/bin/env python3
vol1 = []
vol2= []
numbers = [7, 2, 3, 8]
numbers = sorted(numbers, reverse=True)
sum_numbers = sum(numbers)
half_numbers = sum_numbers / 2
for i in numbers:
    if i <= half_numbers:
        vol1.append(i)
        half_numbers -= i
    else:
        vol2.append(i)
print(vol1)
print(vol2)    