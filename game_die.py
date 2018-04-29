from random import randint

class Die():

	def __init__(self,sides):
		self.sides = sides

	def throw_time(self,times):
		number = []
		count = 1
		while count <= times:
			count += 1
			num = randint(1,self.sides)
			if num % 3 == 0:
				print ("The number is: " + str(num) +", you are die!")
				number.append(num)
				break
			else:
				print ("You are lucky: " + str(num) + "!")
				number.append(num)
		print (number)

chance = Die(10)
chance.throw_time(10)