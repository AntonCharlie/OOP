
class Dog:

	owner = "Charlie" # attribute di luar init yg tdk berubah
	
	def __init__(self, name): # fungsi konstruktor
		self.name = name
		self.age = 0 #month
		self.isCute = True

	def sit(self):
		print(f"{self.name} is sitting right now.")


	def roll_over(self):
		print(f"{self.name} rolled over")

	def sleep(self):
		print(f'{self.name} : "zzzz"')


		# variable, list, dictionary --> attribute
		# function --> method / ability

moly = Dog(name="Moly") 	


moly.sit()
moly.roll_over()
moly.sleep()