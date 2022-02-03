import random
def rps():
	while True:
		print("We'll begin our ROCK PAPER SISSORS game")
		game = ["rock", "paper","sissors"]
		system = random.choice(game)
		player = input("enter your choice ")
		if system == player :
			print(f"""computer's choice was {system.upper()}
It's a TIE			
			        """)
		elif player.lower() == "rock" and system == "sissors":
			print(f"""computer's choice was {system.upper()}
YOU WON 
       					""")
		elif player.lower() == "sissors" and system == "paper":
			print(f""" computer's choice was {system.upper()}
YOU WON 
						""")
		elif player.lower() == "paper" and system == "rock":
			print(f"""computer's choice was {system.upper()}
YOU WON 
						""")
		else:
			print(f"""computer's choice was {system.upper()}
Sorry YOU LOSE 
						""")
		
		
rps()
