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
