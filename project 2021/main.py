from os import system
import json
from getpass import getpass

from pengaturan import Pengaturan
from pengguna import Pengguna
from kontak import Kontak

class Warungku:

	def __init__(self):
		self.pengaturan = Pengaturan()
		#self.active = True

	def load_data(self):
		try:
			with open(self.pengaturan.contacts_location, 'r') as file:
				self.pengaturan.kontak = json.load(file)
		except:
			self.pengaturan.kontak = {}

		try:
			with open(self.pengaturan.users_location, 'r') as file:
				self.pengaturan.users = json.load(file)
		except:
			self.pengaturan.users = {}
		

	def clear_screen(self):
		system("cls")

	def logger(self):
		self.clear_screen()
		self.login_attempts = 0
		while self.login_attempts < 3:
			print("\nPlease login")
			username = input("Username\t: ")
			password = getpass("Password\t: ")

			if username in self.pengaturan.users:
				if self.pengaturan.users[username]["password"] == password:
					self.user = Pengguna(username,
						first=self.pengaturan.users[username]['first'],
						last=self.pengaturan.users[username]['last'],
						password="")
					return True
			else:
				print("Login Gagal")
			self.login_attempts += 1

		return False

	def show_menus(self):
		self.clear_screen()
		print(self.pengaturan.menu)

	def find_contact(self, phone):
		kontak = self.pengaturan.kontak
		if phone in kontak:
			print("Barang ditemukan!")
			print(f"Name : {kontak[phone]['first'].title()} {kontak[phone]['last'].title()} ")
			print(f"Phone : {phone}")
			print(f"Address : {kontak[phone]['address']}")
			return True
		else:
			print("Barang tidak ditemukan")


	def save_data(self):
		with open(self.pengaturan.contacts_location, "w") as file:
			json.dump(self.pengaturan.kontak, file)


	def check_option_user(self, char):
		if char == "q":
			self.pengaturan.active = False
			self.clear_screen()
		elif char == "1":

			self.clear_screen()
			# print(self.settings.contacts)
			kontak = self.pengaturan.kontak
			print(f"Nama\t\tHarga\t\tSatuan\t\tSisa")

			for phone, kontak, in kontak.items():
				print(f"{phone}\t\t{kontak['first'].title()}\t\t{kontak['last'].title()}\t\t{kontak['address']}")
			input("Press Enter to Return.")

		elif char == "2":
			
			self.clear_screen()
			phone = input("Nama barang : ")

			self.find_contact(phone)

			input("Press Enter to Return")

		elif char == "3":
			
			self.clear_screen()
			phone = input("Nama : ")
			first = input("Harga : ")
			last = input("Satuan : ")
			address = input("Sisa : ")

			kontak = Kontak(first, last, phone, address)
			self.pengaturan.kontak[kontak.phone] = {
				"first" : kontak.first,
				"last" : kontak.last ,
				"address" : kontak.address
			}


			self.save_data()

			print("Data disimpan")
			input("Press Enter to Return")


		elif char == "4":

			self.clear_screen()
			phone = input("Nama Barang : ")

			if self.find_contact(phone):
				print("Edit\n1. Nama, 2. Harga, 3. Satuan, 4. Sisa")
				option = input("Mau update yang mana ? (1/2/3/4)")
				if option == "1":
					
					old_contact = self.pengaturan.kontak[phone]
					new_phone = input("Nama baru :")

					self.pengaturan.kontak[new_phone] = {
						"first" : old_contact["first"],
						"last" : old_contact["last"],
						"address" : old_contact["address"]
					}

					del self.pengaturan.kontak[phone]
					self.save_data()
					print("Update selesai")

				elif option == "2":
					
					new_first = input("Harga update : ")
					self.pengaturan.kontak[phone]["first"] = new_first
					self.save_data()
					print("Harga baru disimpan.")


				elif option == "3":
					
					new_last = input("Update satuan : ")
					self.pengaturan.kontak[phone]["last"] = new_last
					self.save_data()
					print("Satuan barang disimpan.")


				elif option == "4":
					
					new_address = input("Update sisa : ")
					self.pengaturan.kontak[phone]["address"] = new_address
					self.save_data()
					print("Jumlah barang diupdate.")

			input("Press Enter to Return")


		elif char == "5":

			self.clear_screen()
			phone = input("Nama barang : ")

			if self.find_contact(phone):
				confirm = input("Yakin mau hapus barang ini ? (y/n)")
				if confirm.lower() == "y":
					del self.pengaturan.kontak[phone]

					self.save_data()
					print("Barang dihapus")


			input("Press Enter to Return")



	def run(self):
		self.load_data()
		self.pengaturan.active = self.logger()

		while self.pengaturan.active:
			self.show_menus()
			self.check_option_user(char = input("Pilihan: ").lower())   

			
if __name__ == '__main__':
	program = Warungku()
	program.run()

