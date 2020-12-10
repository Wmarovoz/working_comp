#!/usr/bin/env python3
import random


vol1 = []
vol2= []
numbers = [random.randint(0, 1000) for i in range(random.randint(10, 100))]
numbers = sorted(numbers, reverse=True)
sum_numbers = sum(numbers)
half_numbers = sum_numbers / 2
print(half_numbers)
for i in numbers:
    if i <= half_numbers:
        vol1.append(i)
        half_numbers -= i
    else:
        vol2.append(i)
print(vol1)
print(vol2)    
print(sum(vol1))
print(sum(vol2))