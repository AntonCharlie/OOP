class Mouth:

	def __init__(self, Infohuman):
		self.sex = Infohuman.sex
		self.number = 1
		self.gigi_kuning = True
		self.lip_color = "pink"

	def describe_sex(self):
		print(f"I'm a {self.sex}")
