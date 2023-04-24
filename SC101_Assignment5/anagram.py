"""
File: anagram.py
Name: Anita
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO: this program finds the anagrams of a word
    """
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        word = input(str("Find anagrams for: "))
        start = time.time()
        if word != EXIT:
            print('Searching...')
            anagrams = find_anagrams(word)
            print(anagrams)
            end = time.time()
            print('----------------------------------')
            print(f'The speed of your anagram algorithm: {end - start} seconds.')
        else:
            break


def read_dictionary():
    dictionary = []
    with open(FILE, 'r') as f:
        for line in f:
            # create a list of vocabulary
            dictionary.append(line.strip())
    return dictionary


def find_anagrams(s):
    """
    :param s: the word input by the user
    :return: a list of the word's anagrams
    """
    anagrams_lst = []
    find_anagrams_helper(s, '', anagrams_lst, [])
    return anagrams_lst


def find_anagrams_helper(word, current_anagram, anagrams_lst, i_lst):
    """
    :param word: the word input by the user
    :param current_anagram: a string to collect the possible anagrams
    :param anagrams_lst: a list of the word's anagrams
    :param i_lst: a list recording the characters' order that has been used
    :return: nonea 
    """
    dictionary = read_dictionary()
    if len(current_anagram) == len(word):
        # avoid anagrams appearing as prefixes of words in the dictionary
        if current_anagram in dictionary:
            print('Found: ' + current_anagram)
            print('Searching...')
            anagrams_lst.append(current_anagram)
    else:
        for i in range(len(word)):
            # record the order of the character
            # instead of comparing the occurrence of the alphabet, this avoids repeated alphabets.
            if i not in i_lst:
                # choose
                i_lst.append(i)
                current_anagram += word[i]
                # explore
                if has_prefix(current_anagram):
                    find_anagrams_helper(word, current_anagram, anagrams_lst, i_lst)
                # un-choose
                current_anagram = current_anagram[:len(current_anagram)-1]
                i_lst.pop()


def has_prefix(sub_s):
    """
    :param sub_s: the prefix of the anagram
    :return: whether there is such word with the prefix in the dictionary (Boolean)
    """
    dictionary = read_dictionary()
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
