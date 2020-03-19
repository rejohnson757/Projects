#03/16/2020
# Practice after comptia exam

'''This program will use Caesar cipher ROT13'''


def rot_13():
	text = input('Please enter a message: ')
	lst = []
	for letter in text:
		letter = ord(letter)
		letter = letter + 13
		if letter > ord('z'):
			(letter - ord('z')) + ord('a')
		lst.append(chr(letter))
		
	print(lst)
	
rot_13()

