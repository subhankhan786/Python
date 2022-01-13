number = int(input("Enter number: \n"))
check = int(number % 2)
odd = int(number % 3)
if check==0:
    print("It's a even number")
elif check!=0 and odd!=0:
    print("It's a prime number") 
else:
    print("It's a odd number")
