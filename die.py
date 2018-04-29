from random import randint

class Die():

	def __init__(self, num_side=6):
		self.num_side = num_side

	def roll(self):
		"""投掷骰子"""
		return randint(1, self.num_side)