from random import choice

class Mouth:

	def __init__(self, Infohuman):
		self.sex = Infohuman.sex
		self.number = 1
		self.gigi_kuning = True
		self.lip_color = "pink"

	def describe_sex(self):
		print(f"I'm a {self.sex}")

class Eye:

	def __init__(self):
		self.number = 2
		self.color = "grey"
		self.is_big = True

class Head:

	def __init__(self, Infohuman):
		self.eyes = Eye()
		self.mouth = Mouth(Infohuman)

class Human:

	def __init__(self, name):

		self.name = name
		self.age = 0
		self.sex = choice(["Male", "Female"])
		self.head = Head(self)


	def describe_me(self):
		print(f"Hello, I'm {self.name} and now I'm {self.age} years old.")


jono = Human(name="jono")
jono.head.mouth.describe_sex()