import random

list = ['1', '2', '3', '4', '5'] # increase the numbers in the list if you want.
user = input("Guess the number: ")
computer = random.choice(list) 

if user == computer:
    print(f"Your no.{user} matches the computer no.{computer}. You wins!")

elif user != computer:
    print(f"Your no.{user} doesn't matches the computer no.{computer}. You lose!")