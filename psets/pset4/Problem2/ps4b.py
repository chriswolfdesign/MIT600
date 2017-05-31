# Problem Set 4
# Chris Wolf
# 2:00

#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    
    savings = []
    years = len(growthRates)
    for year in range(0, years):
        if year == 0:
            savings.append(salary * save * 0.01)
        else:
            savings.append(savings[year - 1] * (1 + 0.01 * growthRates[year]) \
			+ salary * save * 0.01)
    return savings
    
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

testNestEggVariable()
