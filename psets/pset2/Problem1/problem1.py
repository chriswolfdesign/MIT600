# Problem Set 2
# Chris Wolf
# 1:45

def print_order(six_piece, nine_piece, twenty_piece):
    print("Six pieces:", six_piece)
    print("Nine pieces:", nine_piece)
    print("Twenty pieces:", twenty_piece)

def purchase(nuggets):
    for i in range(0, nuggets):
        for j in range(0, nuggets):
            for k in range(0, nuggets):
                if (6*i + 9*j + 20*k == nuggets):
                    print_order(i, j, k)
                    return
    print("No possible combination for this number of nuggets")

num = int(input("How many McNuggets would you like? "))
purchase(num)