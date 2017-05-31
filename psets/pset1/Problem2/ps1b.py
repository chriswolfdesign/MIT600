# Problem Set 1
# Chris Wolf
# 0:45

import math

def prime(num):
    total = math.log(2)
    candidate = 3
    while not candidate == num:
        isPrime = True
        for i in range(2, candidate):
            if candidate % i == 0:
                isPrime = False
        if isPrime:
            total += math.log(candidate)
        candidate += 1
    return total

num = int(input("What is the limit? "))
total = prime(num)
print("num: ", num)
print("total: ", total)
print("ratio: ", total/num)