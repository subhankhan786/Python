import random
list = ['chips', 'cheese', 'chocolate', 'cake', 'icecream']
str = random.choice(list)
sliced = slice(2)
s = print(str[sliced])
user = input("Enter: ")

if user == str:
    print(f"Correct the word is {str}")

else:
    print(f"Wrong the word was {str}")