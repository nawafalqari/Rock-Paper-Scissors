import random

# r > s and s > p and p > r

choices = ['r', 'p', 's']

def play():
	choice = input('Enter rock or paper or scissors (r/p/s): ')
	computer = random.choice(['r', 'p', 's'])	
	if choice == computer:
		print(f'Tie {computer}')
	elif (choice == 'r' and computer == 's') or (choice == 's' and computer == 'p') or (choice == 'p' and computer == 'r'):
		print(f'You won!! the computer chosen {computer}')
	elif choice not in choices:
		print('Wrong choice')
	else:
		print(f'gg noob the computer won {computer}')

play()
