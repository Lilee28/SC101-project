"""
File: boggle.py
Name: Anita Lee
----------------------------------------
TODO: This program finds the possible combinations of alphabets according to the rule of the game 'Boggle'
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO: This program finds the possible combinations of alphabets according to the rule of the game 'Boggle'
	"""
	####################

	alpha_lst = [1, 2, 3, 4]
	illegal = False  # check if the input value is in the right format

	for i in range(1, 5):
		row = input(str(i)+' row of letters: ')
		alpha_lst[i-1] = row.split()  # store a list of alphabets in the alpha_list
		if len(alpha_lst[i-1]) != 4:  # if the row entered does not have 4 alphabet, the format is wrong
			print('Illegal input')
			illegal = True
		else:
			for alpha in alpha_lst[i-1]:
				if len(alpha) != 1:  # if the alphabets are not separated by space, the format is wrong
					print('Illegal input')
					illegal = True
					break  # break the for loop in line 29
		if illegal:
			break  # break the for loop in line 22

	start = time.time()

	if illegal:  # not enough information to run the program
		pass
	else:
		for i in range(4):
			for j in range(4):
				if alpha_lst[i][j].isupper():  # case-insensitive
					alpha_lst[i][j] = alpha_lst[i][j].lower()

		if len(alpha_lst) == 4:  # the format of the input value is correct
			dictionary = read_dictionary()
			num_words = [0]  # use lst so won't be affected by stack frame
			for i in range(4):
				for j in range(4):
					# choose: loop over the 16 possible starting of a word
					alpha = alpha_lst[i][j]
					# explore
					find_words(alpha_lst, i, j, num_words, '', dictionary, [])
					# un-choose
					alpha_lst[i][j] = alpha
			print('There are', num_words[0], 'words in total.')

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def find_words(alpha_lst, lst_num, alpha_num, num_words, word, dictionary, founded):
	"""
	:param alpha_lst: (lst) a nested list of the input value
	:param lst_num: (lst) the index of alpha_lst (vertical index in the 4*4 plane)
	:param alpha_num: (lst) the index of the list in the alpha_lst (horizontal index in the 4*4 plane)
	:param num_words: (lst) a len == 1 list recording the number of words founded
	:param word: (str) a string that compose the word
	:param dictionary: (lst) a list of words in the dictionary
	:param founded: (lst) a list of words that is already founded.
					This avoids a single word being counted more than once
	"""
	if alpha_lst[lst_num][alpha_num]:  # True if the alphabet is not used
		word += alpha_lst[lst_num][alpha_num]  # choose
		alpha_lst[lst_num][alpha_num] = ''  # replace used alphabet with empty string
	if word in dictionary and len(word) > 3 and word not in founded:
		print('Found \"' + word + '\"')
		num_words[0] += 1
		founded.append(word)
	if has_prefix(word, dictionary):  # explore: find the alphabets around the selected alphabet (3*3 plane)
		for i in range(-1, 2):
			if i + lst_num in range(4):  # prevent getting out of the range (0~3)
				for j in range(-1, 2):
					if j + alpha_num in range(4):  # prevent getting out of the range (0~3)
						if alpha_lst[i + lst_num][j + alpha_num]:  # True if the alphabet is not being used
							alpha = alpha_lst[lst_num+i][alpha_num+j]
							find_words(alpha_lst, lst_num+i, alpha_num+j, num_words, word, dictionary, founded)
							alpha_lst[lst_num+i][alpha_num+j] = alpha  # un-choose


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	:return: (lst) a list of words in the dictionary
	"""
	dict_lst = []
	with open(FILE, 'r') as f:
		for line in f:
			dict_lst.append(line.strip())
	return dict_lst


def has_prefix(sub_s, dictionary):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:param dictionary: (lst) a list of words in the dictionary
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
