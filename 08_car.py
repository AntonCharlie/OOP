#inheritance


class Car:

	def __init__(self, make, model, year, color, new, manual):

		self.make = make
		self.model = model
		self.year = year
		self.color = color
		self.new = new
		self.manual = manual
		self.odometer = 0

	def get_descriptive(self):
		return f"This car is a {self.make}'s car.\nIts model is {self.model}-{self.year}.\nIt has {self.color} color"

	def increment_odometer(self, kms):
		self.odometer += kms
		print(f"The odometer has been updated to {self.odometer} kms.")

	def fill_gas_tank(self):
		print("The car is full of fuel now")

	def change_color(self, new_color):
		self.color = new_color
		print(f"The color has been updated to {self.color}")


class ElectricCar(Car):

	#def __init__(self, make, model, year, color, new, manual):
		#super().__init__(make, model, year, color, new, manual)

	def __init__(self, *args, **kwargs):
		#super().__init__(*args, **kwargs)
		Car.__init__(self, *args, **kwargs)

	def fill_gas_tank(self):
		print("This car doesn't need gass..") #overwrite

	def charge_battery(self):
		print("This car has been fully charged") # add special method


class ElectricBus(ElectricCar):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ban = 8
		self.sopir = 1
		self.gogreen = True
		self.big = False

	def small_size(self):
		if self.big == False:
			print("This bus can be enlarged")
			self.big = True

	def fungsi(self):
		print("This bus is used to bring many people.")
	# special attribut => self.anything (livery)
	# special method => def anything(self, *, **) (telolet_om)


trans = ElectricBus("trans", "transjakarta", 2023, "blue", True, True)
print(trans.get_descriptive())
trans.increment_odometer(400)
trans.change_color("yellow")
trans.fill_gas_tank()
trans.charge_battery()
trans.small_size()
trans.fungsi()

hyundai = ElectricCar("hundai", "kona-ev", 2021, "white", True, manual=False)
print(hyundai.get_descriptive())
hyundai.increment_odometer(200)
hyundai.change_color("black")
hyundai.fill_gas_tank()
hyundai.charge_battery()


"""
toyota = Car("toyota", "yaris", 2020, "red", True, True)
print(toyota.get_descriptive())
toyota.increment_odometer(1000)
toyota.fill_gas_tank()
toyota.change_color("black")
"""