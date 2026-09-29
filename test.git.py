print("hello world")
Username = "Mansur"
Password = "fatstinkypoo"


a = input("Enter your username:")
b = input("Enter your password:")

if a == Username:
    if b == Password:
        print("login successful")
    else: print("incorrect Password or Username")
else: print("incorrect Password or Username")