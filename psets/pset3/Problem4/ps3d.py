# Problem Set 3
# Chris Wolf
# 3:00

from string import *

# this is a code file that you can use as a template for submitting your
# solutions

# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

def subStringMatchExact(target, key):
    if target.find(key) == -1:
        return -1
    else:
        answers = ()
        for i in range(0, len(target)):
            if target[i:].find(key) == 0:
                answers = answers + (i,)
    return answers

def constrainedMatchPair(firstMatch, secondMatch, length):
    answers = ()
    for i in firstMatch:
        for j in secondMatch:
            if i + length + 1 == j:
                answers = answers + (i,)
    return answers

### the following procedure you will use in Problem 3

def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
    return allAnswers

def subStringMatchExactlySubOne(target, key):
    all_possible = subStringMatchOneSub(key, target)
    only_correct = subStringMatchExact(target, key)
    one_wrong = ()
    for i in all_possible:
        if not i in only_correct and not i in one_wrong:
            one_wrong = one_wrong + (i,)
    return one_wrong

print(subStringMatchExactlySubOne(target2, key12))