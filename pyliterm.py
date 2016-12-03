###Linux Quest

###Linux Terminal Simulator for those not willing to install Linux or unable to run a Virtual Machine.

###Starting Date: Saturday, December 3rd, 2016. 9:15am CST
###Proposed Closing Date: Saturday, December 3rd, 2016. 9:00pm CST

###Language: Python

###Imports
import time
alllocations = ['~','/home/', "/home",'/','~']
history = ['~']
cdtimes = 1
###The starting location
#location = "~" ## /home/entered name

#Defining what is used in the Terminal
def ssh():
	if moving in alllocations:
		location = ("{}".format(moving))
		return location
	else:
		print("bash: cd: {}: No such file or directory. Moving back to home.".format(moving))
		location = '~'
		return location


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
		ssh(location)
	if 'exit' in userline:
		going = False