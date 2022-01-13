import string 
import random
def pasgen():
    length = int(input("Enter lenght: \n"))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all, length)
    password = "".join(temp)
    print(password)
pasgen()
while True:
    re = input("Regenerate Password?\n")
    if re == "yes":
        pasgen()
    else:
        exit()