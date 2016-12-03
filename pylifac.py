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
