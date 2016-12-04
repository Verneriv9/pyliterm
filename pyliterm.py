###Linux Quest

###Linux Terminal Simulator for those not willing to install Linux or unable to run a Virtual Machine.

###Starting Date: Saturday, December 3rd, 2016. 9:15am CST
###Proposed Closing Date: Saturday, December 3rd, 2016. 9:00pm CST

###Language: Python

###Imports
import time
from tabulate import tabulate
alllocations = ['~','/home/', "/home",'/','~']
history = ['~']
cdtimes = 1
###The starting location
#location = "~" ## /home/entered name

#Defining what is used in the Terminal
def pylifac():
	do = True
	from tabulate import tabulate
	currentdir = "l"
	print("Welcome to the Texas Tech Faculty Listing")
	name = input("root@10.160.1.244: ")
	server = ['ls']
	if name in server:
	    currentdir = "server1"
	if currentdir == "server1":
		print("Faculty.odf")
	while do == True:
	    newname = input("root@10.160.1.244: ").split()
	    if newname[0] == "less":
	        if newname[1] == "Faculty.odf":
	            print(tabulate([['Jane','Alah', ' Professor'], ['Taylor','Brown', 'TA'], ['John','Smith', 'Professor'], ['Sarah','Silver', 'Professor'], ['Seif','Tao', 'TA'], ['Lauren','Ulies', 'Professor'] , ['Martin','Wilson','TA']], headers=['First Name','Last Name', 'Position'], tablefmt='orgtbl'))
	    if newname[0] == "exit":
	        import txtechserver
	        do = False

def texastechserver():
	do = True
	currentdir = "l"
	name = input("root@10.160.1.251: ")
	server = ['ls', 'ssh root@10.160.1.244']

	if name in server:
		currentdir = "server1"

	if currentdir == "server1":
		print("Hint.txt, PW.docx, ClassSchedule.csv, ReadMe.txt")
	while do == True:
		newname = input("root@10.160.1.251: ").split()
		if newname[0] == "less":
			if newname[1]== "ReadMe.txt":
				password = input("*Document Locked* - Enter Password: ")
				if password == "RaiderPower":
					print("Welcome new faculty! To get to your email server, connect via the admin account located at 10.160.1.32")
			if newname[1] == "Hint.txt":
				 print("This is where the information for each document is going to go")
			if newname[1] == "PW.docx":
				 print("This is File 2")
			if newname[1] == "ClassSchedule.csv":
				 print("Notes from IT: To connect to the faculty list, SSH into 10.160.1.244")
		if newname[0] =="ls":
			print("Hint.txt, PW.docx, ClassSchedule.csv")
		if newname[0] =="ssh":
			if newname[1] =="root@10.160.1.244":
				import pylifac
				do = False
			if newname[1] =="admin@10.160.1.32":
				import pylimailserver
				do = False
		if newname[0] =="exit":
			##from pyliterm.py import cd():
			do = False

	##import pylifac


def pylimailserver():
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

def ssh(userline):
#	print(userline)
	if userline[1] =="admin@10.160.1.32":
		import pylimailserver
		pylimailserver()
	if userline[1] =="admin@10.160.1.251":
		import txtechserver
		texastechserver()
	if userline[1] =="admin@10.160.1.244":
		import pylifac
		pylifac()

def firstcd(history, cdtimes, alllocations):
	print("")
	print("CD stands for change directory. Where would you like to go?")
	
	location = input("{}@{} ~ $".format(name, computer)).split()
	moving = location
	#print(moving)
	
	while moving == "":
		location = input("CD stands for change directory. Where would you like to go?").split()
		moving = location
	#print(location)
	if len(moving) != 0:
		moving = moving[1]
		#print(moving)
		location = moving
	if moving in alllocations:
		location = moving
		#print(location)
	else:
		print("bash: cd: {}: No such file or directory. Moving back to home.".format(location[1]))
		location = '~'
	#nameandlocation = ("{} {} $".format(wholename, location))
	return location


def cd(alllocations):
	#print(moving)
	if moving in alllocations:
		location = ("{}".format(moving))
		return location
	else:
		print("bash: cd: {}: No such file or directory. Moving back to home.".format(moving))
		location = '~'
		return location

def cp():
	pass

def firstls(location):
	print("")
	print("Using ls in your current directory will list all items in that folder.")
	firstls = input("{} {} $".format(wholename, location))
	if firstls == "ls":
		pass
	while firstls != "ls":
		print("Using ls in your current directory will list all items in that folder.")
		firstls = input("{} {} $".format(wholename, location))
	if location in ["/"]:
		print("   Home   Locked")
	elif location in ["/home/","/home"]:
		print("   textile.odt   texts.txt   spanish.txt")
	elif location in ["/home/root/", "/home/root", "~"]:
		print("    Empty.ogg")

def ls(location):
	if location in ["/"]:
		print("   Home   Locked")
	elif location in ["/home/","/home"]:
		print("   textile.odt   texts.txt   spanish.txt")
	elif location in ["/home/root/", "/home/root", "~"]:
		print("    Empty.ogg")

def opening():
	print("Welcome to the Linux Terminal Simulator!")
	print("")
	print("The goal of this simulator is to show you how to use basic commands in the Linux Terminal!")
	print("")
	time.sleep(.5)
	print('''Typically in the terminal, the terminal will show you your current username and your computer's name.
The format looks like this: username@computername "location" $''')
	print("")

def name():
	name = input("What would you like your username for this session to be? ").strip("")
	if name == "":
		name = "root"
	print("")
	return name

def computer():
	computer = input("What would you like your computer's name for this session to be? ").strip("")
	if computer == "":
		computer = "localhost"
	return computer

opening()
name = name()
computer = computer()
wholename = "{}@{}".format(name, computer)
print(wholename)
###Settable variables
location = firstcd(history, cdtimes, alllocations)
firstls(location)
###Necessary variables
userhome = ['/home/{}'.format(name), '~', '/home/{}/'.format(name)]
home = ['/home','/home/', 'home']
alllocations.append(userhome[0])
alllocations.append(userhome[2])

going = True
while going:
#	print(location)
	userline = input("{} {} $".format(wholename, location)).split()
	if 'cd' in userline:
		if len(userline) < 2:
			userline = input("{} {} $".format(wholename, location)).split()
		else:
			moving = userline[1]
		location = cd(alllocations)
	if 'ls' in userline:
		ls(location)
	if 'ssh' in userline:
		print('ssh occured')
#		ssh(userline)
	if 'exit' in userline:
		going = False