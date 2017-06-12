# 6.00 Problem Set 6
# Chris Wolf
# 12 hours
# 
# The 6.00 Word Game
#

import random
import string
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

points_dict = {}
time_limit = 0.0

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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

#
# Problem #1: Scoring a word
#
def get_word_score(word):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0.0
    for letter in word:
        score += float(SCRABBLE_LETTER_VALUES[letter.lower()])
    return score

def get_words_to_points(word_list):
    """
    Returns a dictionary containing our entire word list
    translated into a dictionary, pairing each word with the points the word
    is worth.

    word_list: The array of words created earlier in the program.
    returns: string -> int
    """
    return_dict = {}
    for word in word_list:
        return_dict[word] = get_word_score(word)
    return return_dict

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                              # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = n / 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    freq = get_frequency_dict(word)
    newhand = {}
    for char in hand:
        newhand[char] = hand[char]-freq.get(char,0)
    return newhand
    #return dict( ( c, hand[c] - freq.get(c,0) ) for c in hand )


#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, points_dict):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    freq = get_frequency_dict(word)
    for letter in word:
        if freq[letter] > hand.get(letter, 0):
            return False
    return word in points_dict

def get_time_limit(points_dict, k):
    """
     Return the time limit for the computer player as a function of the
    multiplier k.
     points_dict should be the same dictionary that is created by
    get_words_to_points.
    """
    start_time = time.time()
    # Do some computation. The only purpose of the computation is so we can
    # figure out how long your computer takes to perform a known task.
    for word in points_dict:
        get_frequency_dict(word)
        get_word_score(word)
        end_time = time.time()
    return (end_time - start_time) * k

def create_subsets(hand):
    """
    Takes in a string and returns all possible subsets
    of said string.

    hand: string representing all of the letters in the hand
    return: a list of all possible subsets of the letters in hand
    """

    """ Create all possible subsets """
    subsets = []
    if len(hand) > 1:
        subsets.append(hand[0])
        tmp = create_subsets(hand[1:])
        subsets.extend(tmp)
        for item in tmp:
            subsets.append(hand[0] + item)
    else:
        subsets.append(hand[0])
    return subsets

def play_best_word(hand, points_dict):
    """
    Allows a computer player to play.
    Takes in a hand and our current dictionary
    Plays the best word possible given the tiles in its' hand

    hand: The computer player's current hand
    points_dict: Our current dictionary of playable words

    returns: the word we have chosen to play
    """
    # Set default parameters, and prepare base case (no playable word)
    score = 0
    current_word = "."

    # Compare our hand to every word in points_dict
    for word in points_dict:
        if is_valid_word(word, hand, points_dict) and points_dict[word] > score:
            score = points_dict[word]
            current_word = word

    return current_word

def play_best_word_faster(hand, points_dict):
    """
    A modified version of play_best_word that will ideally perform faster.

    hand: The computer player's current hand
    points_dict: Our current dictionary of playable words

    returns: the word we have chosen to play
    """

    """ Convert hand into a string """
    hand_string = ""
    for letter in hand:
        for i in range(hand[letter]):
            hand_string += letter

    """ Create and organize our list of subsets """
    subsets = create_subsets(hand_string)
    for item in subsets:
        """
        If the item is less than three letters and therefore inelible
        to be a word
        """
        if len(item) < 3:
            subsets.remove(item)
            """ Otherwise, sort the word to be a sorted string """
        else:
            item = "".join(sorted(item))

    """
    Find all possible words but only return the one with the word
    with the greatest value
    """
    best_word = "."
    best_score = 0.0
    for item in subsets:
        if item in points_dict and len(item) > 3:
            if points_dict[item] > best_score:
                best_word = item
                best_score = points_dict[item]

    return best_word

#
# Problem #4: Playing a hand
#
def play_hand(hand, points_dict):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    total = 0.0
    allotted_time = time_limit
    initial_handlen = sum(hand.values())
    while sum(hand.values()) > 0:
        print 'Current Hand:',
        display_hand(hand)
        start_time = time.time()
        userWord = play_best_word_faster(hand, points_dict)
        if userWord == '.':
             break
        else:
            isValid = is_valid_word(userWord, hand, points_dict)
            if not isValid:
                print 'Invalid word, please try again.'
            else:
                points = points_dict[userWord]
                end_time = time.time()
                total_time = end_time - start_time

                if total_time >= allotted_time:
                    print 'It took longer than %f to answer.' % allotted_time,
                    print 'You scored %f points.' % total
                else:
                    print 'It took %f to provide an answer' % total_time
                    if total_time < 1.0:
                        total_time = 1.0

                    points = points / total_time

                    if len(userWord) == initial_handlen:
                        points *= 2

                    total += points
                    print '%s earned %f points. Total: %f points' % (userWord, points, total)
                    hand = update_hand(hand, userWord)
    print 'Total score: %f points.' % total

def get_word_rearrangements(points_dict):
    """
    Takes in a word_dict and organizes each word based on its' letters
    points_dict: the global variable used to store a word and its' points
	returns: a new dictionary that holds the sorted word
	"""
    new_dict = {}
    for word in word_list:
        sorted_word = sorted(word)
        new_dict[''.join(sorted_word)] = points_dict[word]
    return new_dict

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
#
def play_game(points_dict):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """

    hand = deal_hand(HAND_SIZE) # random init
    while True:
        cmd = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), points_dict)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), points_dict)
            print
        elif cmd == 'e':
            break
        else:
            print "Invalid command."

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    points_dict = get_words_to_points(word_list)
    rearrange_dict = get_word_rearrangements(points_dict)
    time_limit = get_time_limit(points_dict, 1)
    play_game(points_dict)

"""
Analysis of algorithm efficiency
--------------------------------

This pset was a large spike in difficulty.  Though this was possible, I am
still unsure whether or not I completed the pset entirely correctly.  The
instructions were vague at times and made completion very difficult.

I am not entirely sure how play_best_word_faster is supposed to be more
efficient than play_best_word.  I believe it is due to the organization of the
letters allowing the words to be found more quickly.  Its' efficiency may also
come from the fact that each letter combination (roughly 60 in a seven letter
hand) is searching through the entire dictionary instead of every word in the
dictionary searching for every combination of letters.  I am realizing that
algorithms are a difficulty for me and I will need to continue studying and
refining my ability to perform these accurately.  I intend to come back and
revise this pset after I have mastered more concepts in Computer Science.  For
now I believe my code to be sufficient even if not entirely accurate.
"""
