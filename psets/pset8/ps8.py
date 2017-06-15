# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name: Chris Wolf
# Collaborators:
# Time:
#

import time

SUBJECT_FILENAME = "subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename):
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    inputFile = open(filename)
    subjects = {}
    for line in inputFile:
        my_line = line.split(",")
        subjects[my_line[0]] = (int(my_line[1]), int(my_line[2]))
    return subjects

def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames.sort()
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print res

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """

    classes = {}
    work_left = maxWork

    # If user chooses to base decisions on the value of the course
    if comparator == "cmpValue":
        best_value = [0, 0]
        best_key = ""
        while True:
            for item in subjects:
                # If current item has better value and we have enough hours
                # left to take this class, keep it
                if cmpValue(subjects[item], best_value) and \
                subjects[item][WORK] <= work_left and not item in classes:
                    best_key = item
                    best_value = subjects[item]

            # If no classes can fit into our schedule
            if best_key == "":
                break

            # Add the class to classes and remove the hours necessary to take
            # the course
            classes[best_key] = subjects[best_key]
            work_left -= subjects[best_key][WORK]

            # Reset storage values for next iteration
            best_value = [0, 0]
            best_key = ""

    # If user chooses to base decisions on the work load of the course
    if comparator == "cmpWork":
        best_work = [0, 500]
        best_key = ""
        while True:
            for item in subjects:
                # If current item has better value and we have enough hours
                # left to take this class, keep it
                if cmpWork(subjects[item], best_work) and \
                subjects[item][WORK] <= work_left and not item in classes:
                    best_key = item
                    best_work = subjects[item]

            # If no classes can fit into our schedule
            if best_key == "":
                break

            # Add the class to classes and remove the hours necessary to take
            # the course
            classes[best_key] = subjects[best_key]
            work_left -= subjects[best_key][WORK]

            # Reset storage values for next iteration
            best_work = [0, 500]
            best_key = ""

    # If user chooses to base decisions on the ratio between value
    # and work load of the course
    if comparator == "cmpRatio":
        best_ratio = [0.0001, 1]
        best_key = ""
        while True:
            for item in subjects:
                # If current item has better value and we have enough hours
                # left to take this class, keep it
                if cmpRatio(subjects[item], best_ratio) and \
                subjects[item][WORK] <= work_left and not item in classes:
                    best_key = item
                    best_ratio = subjects[item]

            # If no classes can fit into our schedule
            if best_key == "":
                break

            # Add the class to classes and remove the hours necessary to take
            # the course
            classes[best_key] = subjects[best_key]
            work_left -= subjects[best_key][WORK]

            # Reset storage values for next iteration
            best_ratio = [0, 500]
            best_key = ""


    return classes

def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = subjects.keys()
    tupleList = subjects.values()
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    subjects = loadSubjects(SUBJECT_FILENAME)
    start_time = time.time()
    maxWork = 15
    classes = bruteForceAdvisor(subjects, maxWork)
    end_time = time.time()
    total_time = end_time - start_time
    print "It took " + str(total_time) + " to find optimal schedule for " + \
        str(maxWork) + " work load."

# Problem 3 Observations
# ======================
#
# 5 hour workload: 0.15 second
# 10 hour workload: 29.2 seconds
# 15 hour workload: unknown, was not willing to wait for computation to finish
# 20 hour workload: unkown, was not willing to wait for computation to finish
#
# This algorithm is clearly unsustainable.  A 5 hour workload does not take
# very long but most universities do not allow students to take less than 8.
# 10 hour workload was also not very long but at my university most students
# take a worload of 15 hours on average.  I am typing this while waiting for
# that computation to be completed.  I started running this implementation
# before I went to the bathroom and I don't particularly have the best diet
# I wanted to determine the time for the maximum workload at my university,
# 20 hours, but I figured the student would probably graduate college before
# the program finished running the computation.
#
# In a real world situation, the advisors would have to e-mail in advance
# with a student to find out how many hours they would like to take and let
# their programs run over night so the student can know their best courses
# before they come in.  Brute force for this application is not the way to go.

#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.

if __name__ == "__main__":
    bruteForceTime()
