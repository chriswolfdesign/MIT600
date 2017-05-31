# Problem Set 3
# Chris Wolf
# 3:00

#!python2

from string import *

def subStringMatchExact(target, key):
    if target.find(key) == -1:
        return -1
    else:
        answers = ()
        for i in range(0, len(target)):
            if target[i:].find(key) == 0:
                answers = answers + (i,)
    return answers

target = raw_input("What is the target string? ")
key = raw_input("What is the key? ")

if subStringMatchExact(target, key) == -1:
    print(key, "is not found in", target)
else:
    print(key, "is found in ", target, "at the following indeces:", \
	subStringMatchExact(target, key))
