chat = {
    'kumar': 1234,
    'saran': 4567
}

name = input("Enter your user name: ")

if name in chat:
    psw = int(input("Enter your password: "))
    if chat[name] == psw:
        print("Yes, you are authenticated")
    else:
        print("Please enter a valid password")
else:
    print("Incorrect user name")