cpass = input("Create PassWord: ")
pfile = open("pass.txt", "a")
pfile.write(cpass)
pfile.close
epass = input("Enter PassWord: ")
pfile = open("pass.txt", "r")
fpass = pfile.read()
if epass==fpass:
	print("Welcome")
	exit()
else:
	print("Wrong PassWord")	
	exit()