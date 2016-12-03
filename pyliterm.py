###Linux Quest

###Linux Terminal Simulator for those not willing to install Linux or unable to run a Virtual Machine.

###Starting Date: Saturday, December 3rd, 2016. 9:15am CST
###Proposed Closing Date: Saturday, December 3rd, 2016. 9:00pm CST

###Language: Python

###Imports
import time
alllocations = ['/home/', "/home",'/']
history = ['~']
cdtimes = 1
###The starting location
#location = "~" ## /home/entered name

#Defining what is used in the Terminal
def ssh():
	pass

def scp():
	pass

def cat():
	pass

def firstcd(history, cdtimes, alllocations):
	print("Time to get a moving grooving going.")
	print("CD stands for change directory. Where would you like to go?")
	location = input("{}@{} ~ $".format(name, computer)).split()
	while location == "":
		location = input("CD stands for change directory. Where would you like to go?").split()
	print(location)
	if len(location) != 0:
		location = location[1]	
		
	if location[1] not in alllocations:
		print("bash: cd: {}: No such file or directory".format(location[1]))
		location = history[cdtimes-1]
	nameandlocation = ("{} {} $".format(wholename, location))
	cdtimes += 1
	history.append(location)
	print(history)
	return location
	return cdtimes

def cd(history, cdtimes, alllocations):
	print(moving)
	if moving in alllocations:
		location = ("{}".format(moving))
		history.append(location)
		cdtimes += 1
		print(cdtimes)
		return location, cdtimes
	else:
		print("bash: cd: {}: No such file or directory".format(moving))
		cdtimes += 1
		location = history[cdtimes-1]
		return location


def cp():
	pass

def ls():
	pass

def location():
	pass

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
###Necessary variables
userhome = ['/home/{}'.format(name), '~', '/home/{}/'.format(name)]
home = ['/home','/home/', 'home']
alllocations.append(userhome[0])

going = True
while going:
	print(location)
	userline = input("{} {} $".format(wholename, location)).split()
	if 'cd' in userline:
		moving = userline[1]
		location = cd(history, cdtimes, alllocations)
	if 'ls' in userline:
		ls()
	if 'exit' in userline:
		going = False