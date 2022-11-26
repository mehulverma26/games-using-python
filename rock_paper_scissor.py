import random
a=0
d='yes'
while d=='yes' or d=='y' or d=='Yes':
	print("you can choose between rock , paper or scissors")
	choice=input("your choice is: ")
	print("My choose",choice)
	computer_choice=random.randint(1,3)
	if computer_choice==1:
		computer_choice='rock'
	elif computer_choice==2:
		computer_choice='paper'
	elif computer_choice==3:
		computer_choice='scissors'
	print("Computer choice is",computer_choice)
	if choice=='rock' or choice=='1':
		if computer_choice=='rock':
			print("It is a tie")
			b='tie'
		elif computer_choice=='paper':
			print("You lose, sorry :( ")
			b='lost'
		elif computer_choice=='scissors':
			print("You win!!!! congrats :) ")
			b='win'
	elif choice=='paper' or choice=='2':
		if computer_choice=='paper':
			print("It is a tie")
			b='tie'
		elif computer_choice=='rock':
			print("You win!!!! congrats :) ")
			b='win'
		elif computer_choice=='scissors':
			print("You lose, sorry :( ")
			b='lost'
	elif choice=='scissors' or choice=='3':
		if computer_choice=='scissors':
			print("It is a tie")
			b='tie'
		elif computer_choice=='rock':
			print("You lose, sorry :( ")
			b='lost'
		elif computer_choice=='paper':
			print("You win!!!! congrats :) ")
			b='win'
	else:
		print("invalid choice!")
		b='invalid'
	if b=='win':
		a=a+1
	elif b=='tie':
		a=a+0
	elif b=='lost':
		a=a-1
	elif b=='invalid':
		a=a+0
	print("your current score is",a)	
	d=str(input("Do you want to try again?(y/n): "))
if d=='no' or d=='n' or d=='No':
	print("Thanks for playing!!!")
	print("your final score is",a)