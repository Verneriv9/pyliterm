do = True
from tabulate import tabulate
currentdir = "l"
name = input("admin@10.160.1.32 ")
server = ['ls']

if name in server:
    print("Texas Tech Mail Accounts")
    print("------------------------")
    print(tabulate([['Jane','Alah', ' LOCKED'], ['Taylor','Brown', 'LOCKED'], ['John','Smith', '105mb'], ['Sarah','Silver', '256mb'], ['Seif','Tao', 'LOCKED'], ['Lauren','Ulies', 'LOCKED'] , ['Martin','Wilson','LOCKED']], headers=['First Name','Last Name', 'MailBox'], tablefmt='orgtbl'))
    print("Please Navigate to /mailbox/ to log in!")
newname = input("root@10.160.1.244: ").split()
if newname[0] == "cd":
    if newname[1] =="/mailbox/":
        print("Welcome to Texas Tech Remote Mail Server")
        email = input("Please Enter Your Email Address: ")
        if email == "john.smith@ttu.edu":
            print("You're in")
