from mouth import Mouth
from eye import Eye

class Head:

	def __init__(self, Infohuman):
		self.eyes = Eye()
		self.mouth = Mouth(Infohuman)
