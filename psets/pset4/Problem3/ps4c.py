# Problem Set 4
# Chris Wolf
# 2:00

#
# Problem 3
#

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
            

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print(savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

testPostRetirement()
