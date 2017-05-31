# Problem Set 2
# Chris Wolf
# 1:45

def find_impossible_order():
    largest = 0
    sequence = 0
    for nuggets in range(1, 200):
        possible_order = False
        for six in range(0, nuggets):
            for nine in range(0, nuggets):
                for twenty in range(0, nuggets):
                    if (6*six + 9*nine + 20*twenty) == nuggets:
                        possible_order = True
        if possible_order:
            sequence += 1
        else:
            largest = nuggets
            sequence = 0
        
        if sequence >= 6:
            return largest

    return "No Solution"
print("Largest number of McNuggets that cannot be bought in exact quantity:", \
find_impossible_order())
