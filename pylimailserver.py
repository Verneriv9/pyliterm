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
            print("Welcome John Smith:")
            while do == True:
                command = input("Jsmith@10.160.1.244: ").split()
                if command[0] == 'cd':
                    if command[1] == "Sent":
                        print(tabulate([['1','Jane','Alah', 'Lunch Today?'] , ['2', 'Lacie','Jones','Thanks for your help :)']], headers=['Email ID','First Name','Last Name', 'Subject'], tablefmt='orgtbl'))
                if command[0] == 'less':
                    if command[1] == "1":
                        print("""Hey John,
                        Did you want to grab some lunch with me today?
                        Your friend, Jane""")
                    if command[1] == "2":
                        print("""Dr.Smith,
                        I wanted to thank you for bumping my grade to an A. When my friends told me you would take me from an F to an A for $1000 I told them no way!
                        Its awesome that you let your students pay for the grade they deserve because after all, we arrrree paying you to let us graduate!

                        With love,
                        Lacie""")
                if command[0] == 'ls':
                    print("Sent", "Recieved", "Deleted")
                if command[0] == 'exit':
                    import pylimailserver
                    do = False
