#!/usr/bin/env python3
import random 
choice = input("Would you like to play a game? y\n") 
rps = {"rock":1, "paper":2, "scissors":3} 
if choice == "y": 
	answer = input("Choose rock, paper, or scissors: ") 
	our_choice = random.choice(["rock", "paper", "scissors"]) 
print(choice, our_choice)

if answer:
	if answer == our_choice:
		print("draw")
	else:
		if answer == "rock" and our_choice == "paper":
		    print ("you lose")
                elif our_choice == "scissors":
		    print("you won")
		if answer == "paper" and our_choice == "scissors":
		    print ("you lose")
		elif our_choice == "paper":
		    print("you won")
		if answer == "scissors" and  our_choice == "paper":
		    print ("you won")
		elif our_choice == "rock":
		    print("you lose")
else:
	print("You did not provide a choice")
