# Problem Set 5: Ghost
# Name: Chris Wolf
# Collaborators: None
# Time: 2.5 hrs
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

def check_word_frag(prefix):
    for item in wordlist:
        if item.startswith(prefix.lower()):
            return True
    return False

def check_complete_word(word):
    if word in wordlist:
        return True
    else:
        return False

def play_game():
    current_word = ""
    game_won = False
    current_player = 1
    next_letter = ""
    
    print "Welcome to Ghost:"
    print "Player 1 goes first"
    print "Current word fragment: ''"
    
    while not game_won:
        
        if current_player == 1:
            next_letter = raw_input("Player 1 says: ")
        else:
            next_letter = raw_input("Player 2 says: ")
        
        current_word += next_letter.upper()
        
        if check_complete_word(current_word.lower()) and len(current_word) > 3:  
            game_won = True
            if current_player == 1: 
                print "Player one loses because '" + current_word + \
                    "' is a word!"
                print "Player two wins!"
            else:
                print "Player two loses because '" + current_word + \
                    "' is a word!"
                print "Player one wins!"
        
        if not check_word_frag(current_word):
            game_won = True
            if current_player == 1:
                print "Player one loses because no word begins with '" + \
                    current_word + "'!"
                print "Player two wins!"
            else:
                print "Player two loses because no word begins with '" + \
                    current_word + "'!"
                print "Player one wins!"
        
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1
        
        if not game_won:
            
            # new line
            print " "
            
            print "Current word fragment: " + current_word
            
            if current_player == 1:
                print "Player one's turn."
            else:
                print "Player two's turn."
    
if __name__ == ("__main__"):
    play_game()