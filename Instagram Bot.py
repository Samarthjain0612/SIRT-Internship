from time import sleep
from getpass import getpass
from instabot import Bot

my_bot = Bot()

print("\n\nWelcome to Instagram Bot\n")
sleep(2)
print("Setting up the connection with https://www.instagram.com/", end = "")
for i in range(3):
    sleep(1.2)
    print('.', end="")

print("\n")
sleep(1.5)
print("Connection established!!!")


username = input("Username : ")
pwd = getpass(prompt="password : ")

# my_bot.login(username = username, password = pwd)

print("\nLogged in successfull")


while True:
    print("\nChoose the options given below\n")
    print("""press 1 to follow
press 2 to unfollow
press 3 to send message
press 4 to exit the app\n""")
    print("Enter the operation you want : ")
    inp  = int(input())
    if inp == 1:
        user = input("Enter the username : ")
        # my_bot.unfollow(user)
        print("successfully followed")
    elif inp == 2:
        user = input("Enter the username : ")
        # my_bot.follow(user)
        print("successfully unfollowed")
    elif inp == 3:
        user = input("Enter Username : ")
        message = input("Enter the message-\n")
        # my_bot.send_message(message, user)
        print("Message sent successfully")
    elif inp == 4:
        # my_bot.logout()
        print("Logging out", end="")
        for i in range(3):
            sleep(1.2)
            print('.', end="")
        print("\n")
        sleep(1.5)
        print("Connection ended!!!")
        print("Logging out successfully")
        break
    else:
        print("Wrong input choose again")