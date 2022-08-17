"""
File: coin_flip_runs.py
Name: 李知穎
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO: This program will simulate coin flip(s) with the number of runs specified by the user.
	"""
	print("Let's flip a coin!")
	# the user will specify the number of runs
	number = input("Number of runs: ")
	string = ""
	# get the first character randomly
	string = flip(string)
	while True:
		# it will keep on flipping the coin until the number of runs reaches the value entered by the user
		string = flip(string)
		run = check_run(string)
		if run == int(number):
			break
	# it will print out the simulated coin flip(s)
	print(string)


def flip(string1):
	"""
	:param string1: the original string
	:return: the updated string with a character added
	"""
	# produce a outcome randomly (either 1 or 2)
	coin = r.randint(1, 2)
	if coin % 2 == 0:
		# if the outcome is 2, the string will add the character "H"
		string1 += "H"
	else:
		# if the outcome is 1, the string will add the character "T"
		string1 += "T"
	return string1


def check_run(s):
	"""
	:param s: the string
	:return: number of runs in the string
	"""
	run = 0
	for i in range(len(s)):
		# it will check through all the characters
		if i != 0 and i != len(s)-1 and s[i] == s[i-1] and s[i] != s[i+1]:
			"""
			if the character meets the following conditions:  
			1. not the first or the last character of the string
			2. same as the previous character 
			3. different from the following character 
			then the number of runs will increase by 1
			"""
			run += 1
		elif len(s) == 2 and i == 0 and s[i] == s[i+1]:
			# under a specific situation that there is only two characters and the two are the same, the run will be 1
			run = 1
		elif i == len(s)-1 and s[i] == s[i-1]:
			# another situation when a run occur at the end of the string
			run += 1
	return run






# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
