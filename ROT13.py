#03/16/2020

'''This program will use Caesar cipher ROT13'''


def rot_13(messge):
	text = input('Please enter a message: ')
	for letter in text:
		letter = ord(letter)
		letter = letter + 13
		if letter > ord('z'):
			(letter - ord('z')) + ord('a')
	print(letter)
	
rot_13('hello')

