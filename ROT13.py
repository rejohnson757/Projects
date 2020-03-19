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
			change = letter - ord('z')
			letter = ord('a') + change - 1
		lst.append(chr(letter)) 
		
	lst = ''.join(lst)
	print(str(lst))
	
rot_13()
