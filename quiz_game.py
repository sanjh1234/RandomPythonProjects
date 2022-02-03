def quiz_game():
	x = 1
	while x == 1:
		player_name = input("""Welcome To the QUIZ GAME
enter players name """)
		game = input("Do You Wanna Play The Game?  ")
		if game.lower() == "no" :
			print ("Okay we'll end our game :)")
			quit()
		elif game.lower() == "yes":
			print("""Okay, got it let's play the quiz game 
If you want to know the rules of the game type rules or type start
			         """)
			start = input("Do you want to know the rules or start the game ")
			if start == "rules":
				print("""Here are the rules of the quiz
You'll get 10 questions and each question contain 10 marks 
At the end of the quiz your total score will be calculated 
Those who have scored more than 50 will win the quiz
						""")
			score = 0
			q1 = input("Who is the father of our Nation? ")
			if q1.lower() == "mahatma gandhi":
				score+=10
				print("correct")
			else:
				print("wrong")
			q2 = input("Who is the first prime minister of India? ")
			if q2.lower() == "jwaharlal nehru":
				score+=10
				print("correct")
			else:
				print("wrong")
			q3 = input("Who is the first president of India? ")
			if q3.lower() == "rajendra prasad":
				score+=10
				print("correct")
			else:
				print("wrong")
			q4 = input("Which day is celebrated as yoga day? ")
			if q4.lower() == "21 june":
				score+=10
				print("correct")
			else:
				print("wrong")
			q5 = input("Who is the current president of India? ")
			if q5.lower() == "ramnath kovind":
				score+=10
				print("correct")
			else:
				print("wrong")
			q6 = input("Who is the current CM of Jharkhand? ")
			if q6.lower() == "hemant soren":
				score+=10
				print("correct")
			else:
				print("wrong")
			q7 = input("Who shot Mahatama Gandhi? ")
			if q7.lower() == "nathuram godse":
				score+=10
				print("correct")
			else:
				print("wrong")
			q8 = input("when was Mahatma Gandhi born? ")
			if q8.lower() == "2 october":
				score+=10
				print("correct")
			else:
				print("wrong")
			q9 = input("Who is known as father of computer? ")
			if q9.lower() == "charles babbage":
				score+=10
				print("correct")
			else:
				print("wrong")
			q10 = input("Who invented electric bulb? ")
			if q10.lower() == "thomas alva edison":
				score+=10
				print("correct")
			else:
				print("wrong")
# print no of questions user got correct
# try using str(score) as in video
			if score < 50 :
				print(f"""Sorry {player_name}, you failed :( 
your total score is {score} 
Better luck next time
						""")
			elif score >= 50 and score < 80:
				print(f"""You did well {player_name}, but you can do better :)
your total score is {score}
hope you work hard
						""")
			elif score >=80 and score < 100:
				print(f"""You have done very well {player_name}, you just need to polish your skills
your total score is {score}
hope you rock next time :)
						""")
			else:
				print(f"""EXCELLENT {player_name.upper()} 
your total score is {score} 
I knew it :)
						""")
		else:
			print(f"Sorry, I didn't got it {player_name}")
		
		
print(quiz_game())