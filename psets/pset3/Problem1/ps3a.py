# Problem Set 3
# Chris Wolf
# 3:00

from string import *

def countSubStringMatch(key, target):
    times_found = 0
    for i in range(len(target)):
        if target[i:].find(key) == 0:
            times_found += 1
    return times_found

def countSubStringMatchRecursive(key, target):
    if len(key) == len(target):
        if target.find(key) == 0:
            return 1
        else:
            return 0
    else:
        if target.find(key) == 0:
            return 1 + countSubStringMatchRecursive(key, target[1:])
        else:
            return 0 + countSubStringMatchRecursive(key, target[1:])

key = raw_input("What is the key? ")
target = raw_input("What is the target? ")

print("Iterative:")

if countSubStringMatch(key, target) == 1:
    print(key, "appears in", target, "one time.")
else:
    print(key, "appears in", target, countSubStringMatch(key, target), "times.")

print("Recursive:")

if countSubStringMatchRecursive(key, target) == 1:
    print(key, "appears in", target, "one time.")
else:
    print(key, "appears in", target, \
	countSubStringMatchRecursive(key, target), "times.")
