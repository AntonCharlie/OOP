"""
Human  -> Head -> Eye (jumlah = 2, warna pupil = "kuning"), Mouth, Nose
	   -> Body -> Leg, (kiri dn kanan), Hand, Torso
"""
from random import choice

class Mouth:

	def __init__(self):
		self.number = 1
		self.gigi_kuning = True
		self.lip_color = "pink"

class Eye:

	def __init__(self):
		self.number = 2
		self.color = "grey"
		self.is_big = True

class Head:

	def __init__(self):
		self.eyes = Eye()
		self.mouth = Mouth()

class Human:

	def __init__(self, name):

		self.name = name
		self.age = 0
		self.sex = choice(["Male", "Female"])
		self.head = Head()


	def describe_me(self):
		print(f"Hello, I'm {self.name} and now I'm {self.age} years old.")


edbert = Human(name="edbert")
edbert.describe_me()
print(edbert.head.eyes.number)

danish = Human(name="danish")	   
danish.describe_me()