

class Car:

	def __init__(self, name, produsen, color, height, price):
		self.name = name
		self.produsen = produsen
		self.color = color
		self.height = height
		self.price = price

	def get_descriptive(self):
		print(f"{self.name} dibuat oleh perusahaan {self.produsen}. \nBiasanya orang membeli mobil ini yang berwarna {self.color}, ketingian mobil ini adalah {self.height}cm. \nMobil ini dibanderol dengan harga {self.price}juta")
		print()



jazz = Car("Jazz", "Honda", "putih", "152", "295" )
Innova = Car("Innova", "Toyota", "silver", "179", "326")
Fortuner = Car("Fortuner", "Toyota", "hitam", "183", "493")
hi_max = Car("Hi max", "Daihatsu", "putih", "285", "107")
ertiga = Car("Ertiga", "Suzuki", "merah", "169", "201")

jazz.get_descriptive()
Innova.get_descriptive()
Fortuner.get_descriptive()
hi_max.get_descriptive()
ertiga.get_descriptive()

