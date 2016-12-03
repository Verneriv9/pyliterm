###Linux Quest

###Linux Terminal Simulator for those not willing to install Linux or unable to run a Virtual Machine.

###Starting Date: Saturday, December 3rd, 2016. 9:15am CST
###Proposed Closing Date: Saturday, December 3rd, 2016. 9:00pm CST

###Language: Python

###Imports
import time

###The starting location
#location = "~" ## /home/entered name

#Defining what is used in the Terminal
def ssh():
	pass

def scp():
	pass

def cat():
	pass

def firstcd():
	print("Time to get a moving grooving going.")
	print("CD stands for change directory. Where would you like to go?")
	location = input("{} ~ $".format(wholename)).split()
	while location == "":
		location = input("CD stands for change directory. Where would you like to go?").split()
	nameandlocation = ("{} {} $".format(wholename, location[1]))
	print(nameandlocation)

def cp():
	pass

def ls():
	pass

def location():
	pass

def naming():
	print("Welcome to the Linux Terminal Simulator!")
	print("")
	print("The goal of this simulator is to show you how to use basic commands in the Linux Terminal!")
	print("")
	time.sleep(.5)
	print('''Typically in the terminal, the terminal will show you your current username and your computer's name.
The format looks like this: username@computername "location" $''')
	print("")
	
	name = input("What would you like your username for this session to be? ").split()
	while name == "":
		name = input("What would you like your username for this session to be? ").split()
	print("")
	computer = input("What would you like your computer's name for this session to be? ").split()
	while computer == "":
		computer = input("What would you like your computer's name for this session to be? ").split()
	wholename = "{}@{}".format(name[0], computer[0])
	print(wholename)
	return wholename

###Settable variables
wholename = naming()
location = "~"
location = firstcd()