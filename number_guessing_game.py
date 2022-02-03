import random
def number_guess():
	x =1
	while x==1:
		number = random.randint(1,10)
		start = print("""

HELLO! Welcome To 
THE GUESSING GAME
					""")
		level = input("""you have to guess between 1-10
Choose your game level
EASY MEDIUM DIFFICULT > """)
# give user hint if she is above the number or below the number 
		if level.lower() == "difficult":
			for chances in range(3):
				guess = int(input ("guess the number > "))
				if number == guess :
					print("HURRAY! YOU WON THE GAME")
					break
				elif chances==2 and number != guess:
					print("""you guessed wrong :(
you lose the game
							""")
				else:
					print("""You have guessed wrong
but the good part is
you have got another chance
							 """)
		elif level.lower() == "medium":
			for chances in range(5):
				guess = int(input ("guess the number > "))
				if number == guess :
					print("HURRAY! YOU WON THE GAME")
					break
				elif chances==4 and number != guess:
					print("""you guessed wrong :(
you lose the game
							""")
				else:
					print("""You have guessed wrong
but the good part is
you have got another chance
							 """)
		elif level.lower() == "easy":
			for chances in range(7):
				guess = int(input ("guess the number > "))
				if number == guess :
					print("HURRAY! YOU WON THE GAME")
					break
				elif chances==6 and number != guess:
					print("""you guessed wrong :(
you lose the game
							""")
				else:
					print("""You have guessed wrong
but the good part is
you have got another chance
							 """)
		else:
			print("""Sorry system don't recognise this level""")
				

number_guess()	