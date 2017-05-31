# Problem Set 1
# Chris Wolf
# 0:45

def prime(num):
    count = 0
    candidate = 3
    
    while not count == num:
        isPrime = True
        for i in range(3, candidate):
            if candidate % i == 0:
                isPrime = False
        if isPrime:
            count += 1
        if count == num:
            return candidate
        else:
            candidate += 1
    
num = int(input("Which prime number would you like? "))
print(prime(num))
