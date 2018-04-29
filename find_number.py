filename = 'pi_million_digits.txt'

with open(filename) as f:
	contents = f.read()

pi_string = ''
for content in contents:
	pi_string += content

number = input("Enter a list of number and it will find it in million pi!!: ")

if number in pi_string:
	site_number = pi_string.find(number)
	print (site_number)
else:
	print ('The number can not find it.')