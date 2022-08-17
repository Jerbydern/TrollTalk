#Dave Strider's Hash Map Fetch Modus

captchaGame = 'Y'
cardNum = 10
inv = {0:' ', 1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ',9:' '}


def stairsBro():
	print ()
	print ('I WARNED YOU ABOUT STAIRS BRO')
	print ()
	print ()
	print ('I TOLD YOU DOG')
	print()
	return

def checkInv():
	print()
	print('Captchalogue:')
	for x in inv:
		print (x,":",inv[x])



def vowelHash(x):
	if len(x) != 1:
		return "error"
	#This would be a good place to implement more advanced error protocol once some is learned. This approach seems more likely to cause harm than help lol.
	if x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
		return 1
	elif x == " ":
		return 0
	return 2



def score (word):
	#This function checks each individual character of the word to return the slot number it corresponds to. This is the 'hash' function.
	x = len(word)
	total = 0
	while x > 0:
		total += vowelHash(word[x - 1])
		x -= 1
	final = total % cardNum
	return final

def scoreFor (word):
	#Same as above but using a for loop, superior for this application
	total = 0
	for x in word:
		total += vowelHash(x)
	final = total % cardNum
	return final


def captchalogue (word):
	#This is where the object is added to the sylladex.
	word = word.upper()
	x = scoreFor (word)
	if word == 'STAIRS':
		stairsBro()
		return ' '

	if inv[x] == ' ':
		inv[x] = word
		print ()
		print ("The", word, "is captchalogued in slot", x)
		print ()
		return
	else:
		print ()
		print ("The", inv[x], "in slot", x, "is ejected and replaced with the", word)
		print ()
		inv[x] = word


def captcha():
	go = 1
	while go == True:
		item = input ("What would you like to Captchalogue?: ").upper()
		if item == "STOP":
			break
		if item == "CHECK INV":
			checkInv()


		else:
			captchalogue(item)

captcha()



"""Okay, so, here are some ideas for where we can go with this

* Set up system that actually keeps track of which cards are where and ejects items when they're replaced. √√√
* Set up a way to display the current inventory √√√
* Create save file


* Set up graphical interface
* Create a small set of objects for player to choose from to add to sylladex
* Make it so that when something gets put into a sylladex card that's already full, the previous thing launches out with an animation
* (This one would be super advanced and hilarious if it worked) Set it up so whatever someone typed, the first image that comes up on google image is what gets put into the sylladex card. """