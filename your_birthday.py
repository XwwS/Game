filename = 'pi_million_digits.txt'

with open(filename, 'r') as file_object:
	contents = file_object.read()

pi_string = ''
for content in contents:
	pi_string += content

number = input("Enter 'q' quit  the game.")
while True:
	birthday = input("Please, enter your birthday: yy/mm/dd: ")
	if birthday in pi_string:
		print ("\tYei, O, baby, you are Lucky!\n")
	elif birthday == 'q':
		print ("The test is break.")
		break
	else:
		print ("\tO, you are not lucky........\n")
