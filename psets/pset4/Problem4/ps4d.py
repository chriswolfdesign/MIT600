# Problem Set 4
# Chris Wolf
# 2:00

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

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """

    balance = []
    years = len(growthRates)
    for year in range(0, years):
        if year == 0:
            balance.append(savings * (1 + 0.01 * growthRates[year]) - expenses)
        else:
            balance.append(balance[year - 1] * (1 + 0.01 * growthRates[year]) \
			- expenses)
    return balance

def findMaxExpenses(salary, save, preRetireGrowthRates, \
postRetireGrowthRates, epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    moneyMade = nestEggVariable(salary, save, preRetireGrowthRates)
    maximum = moneyMade[-1]
    balance = 1000
    highestSpent = (maximum + epsilon) / 2
    lowestSpent = 0
    expenditure = []
    while (abs(balance) > epsilon):
        expenses = (highestSpent + lowestSpent) / 2
        expenditure = postRetirement(maximum, postRetireGrowthRates, expenses)
        balance = expenditure[-1]
        if balance > 0:
            lowestSpent = expenses
        else:
            highestSpent = expenses
    return expenses

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print(expenses)
    # Output should have a value close to:
    # 1229.95548986

testFindMaxExpenses()
