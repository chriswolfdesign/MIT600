# Problem Set 2
# Chris Wolf
# 1:45

def find_least(x, y, z):
    if x < y and x < z:
        return x
    if y < x and y < z:
        return y
    if z < x and z < y:
        return z

def find_impossible_order(x, y, z):
    largest = 0
    sequence = 0
    for nuggets in range(1, 200):
        possible_order = False
        for x_counter in range(0, nuggets):
            for y_counter in range(0, nuggets):
                for z_counter in range(0, nuggets):
                    if (x*x_counter + y*y_counter + z*z_counter) == nuggets:
                        possible_order = True
        if possible_order:
            sequence += 1
        else:
            largest = nuggets
            sequence = 0
        
        if sequence >= find_least(x, y, z):
            return largest

    return "No Solution"

x = int(input("Enter the first nugget size: "))
y = int(input("Enter the second nugget size: "))
z = int(input("Enter the third nugget size: "))

print("Given package sizes", x, y, "and", z, \
"the largest possible number of McNuggets " \
"that cannot be bought in exact quantity is", \
find_impossible_order(x, y, z))
