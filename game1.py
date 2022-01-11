import random

signs = ['rock', 'paper', 'scissor']
computer = random.choice(signs)


user = input('Enter your sign: ')




if user == computer:
  print(f"your choice {user} and computer's choice {computer} are same. It's a tie!")

elif user == 'rock':
    if computer == 'paper':
      print(f"Your choice {user} and computer's choice {computer}. Computer wins!")
    else:
      print(f"Your choice {user} and computer's choice {computer}. You wins!")

elif user == 'paper':
    if computer == 'scissor':
      print(f"Your choice {user} and computer's choice {computer}. Computer wins!")
    else:
        print(f"Your choice {user} and computer's choice {computer}. You wins!") 
    
elif user == 'scissor':
  if computer == 'rock':
    print(f"Your choice {user} and computer's choice {computer}. Computer wins!")
  else:  
    print(f"Your choice {user} and computer's choice {computer}. You wins!")  
  