from tabulate import tabulate
print tabulate([['Jane','Alah', ' Professor'], ['Taylor','Brown', 'TA'], ['John','Smith', 'Professor'], ['Sarah','Silver', 'Professor'], ['Seif','Tao', 'TA'], ['Lauren','Ulies', 'Professor'] , ['Martin','Wilson','TA']], headers=['First Name','Last Name', 'Position'], tablefmt='orgtbl')
