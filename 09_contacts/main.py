from os import system
import json
from getpass import getpass

from settings import Settings
from user import User
from contacts import Contacts

class ContactApp:

	def __init__(self):
		self.settings = Settings()
		#self.active = True

	def load_data(self):
		try:
			with open(self.settings.contacts_location, 'r') as file:
				self.settings.contacts = json.load(file)
		except:
			self.settings.contacts = {}

		try:
			with open(self.settings.users_location, 'r') as file:
				self.settings.users = json.load(file)
		except:
			self.settings.users = {}
		#print(self.settings.contacts, self.settings.users)

	def clear_screen(self):
		system("cls")

	def logger(self):
		self.clear_screen()
		self.login_attempts = 0
		while self.login_attempts < 3:
			print("\nPlease login")
			username = input("Username\t: ")
			password = getpass("Password\t: ")

			if username in self.settings.users:
				if self.settings.users[username]["password"] == password:
					self.user = User(username,
						first=self.settings.users[username]['first'],
						last=self.settings.users[username]['last'],
						password="")
					return True
			else:
				print("Login Failed")
			self.login_attempts += 1

		return False

	def show_menus(self):
		self.clear_screen()
		print(self.settings.menu)

	def find_contact(self, phone):
		contacts = self.settings.contacts
		if phone in contacts:
			print("Contact found!")
			print(f"Name : {contacts[phone]['first'].title()} {contacts[phone]['last'].title()} ")
			print(f"Phone : {phone}")
			print(f"Address : {contacts[phone]['address']}")
			return True
		else:
			print("Contact doesn't exist")


	def save_data(self):
		with open(self.settings.contacts_location, "w") as file:
			json.dump(self.settings.contacts, file)


	def check_option_user(self, char):
		if char == "q":
			self.settings.active = False
		elif char == "1":

			self.clear_screen()
			# print(self.settings.contacts)
			contacts = self.settings.contacts
			print(f"Nomor\t\tNama Lengkap\t\tAlamat")

			for phone, contact, in contacts.items():
				print(f"{phone}\t\t{contact['first'].title()} {contact['last'].title()}\t\t{contact['address']}")
			input("Press Enter to Return.")

		elif char == "2":
			
			self.clear_screen()
			phone = input("Enter phone number : ")

			self.find_contact(phone)

			input("Press Enter to Return")

		elif char == "3":
			
			self.clear_screen()
			first = input("First : ")
			last = input("Last : ")
			phone = input("Phone : ")
			address = input("Address : ")

			contact = Contacts(first, last, phone, address)
			self.settings.contacts[contact.phone] = {
				"first" : contact.first,
				"last" : contact.last ,
				"address" : contact.address
			}


			self.save_data()

			print("Contact saved")
			input("Press Enter to Return")


		elif char == "4":

			self.clear_screen()
			phone = input("Phone : ")

			if self.find_contact(phone):
				print("Edit\n1. Phone, 2. First, 3. Last, 4. Address")
				option = input("Which data do you want to edit / update ? (1/2/3/4)")
				if option == "1":
					
					old_contact = self.settings.contacts[phone]
					new_phone = input("New phone :")

					self.settings.contacts[new_phone] = {
						"first" : old_contact["first"],
						"last" : old_contact["last"],
						"address" : old_contact["address"]
					}

					del self.settings.contacts[phone]
					self.save_data()
					print("New phone number saved.")

				elif option == "2":
					
					new_first = input("New first : ")
					self.settings.contacts[phone]["first"] = new_first
					self.save_data()
					print("New first name saved.")


				elif option == "3":
					
					new_last = input("New last : ")
					self.settings.contacts[phone]["last"] = new_last
					self.save_data()
					print("New last name saved.")


				elif option == "4":
					
					new_address = input("New address : ")
					self.settings.contacts[phone]["address"] = new_address
					self.save_data()
					print("New address has been saved.")

			input("Press Enter to Return")


		elif char == "5":

			self.clear_screen()
			phone = input("Phone : ")

			if self.find_contact(phone):
				confirm = input("Are you sure delete this contact ? (y/n)")
				if confirm.lower() == "y":
					del self.settings.contacts[phone]

					self.save_data()
					print("Contact deleted.")


			input("Press Enter to Return")



	def run(self):
		self.load_data()
		self.settings.active = self.logger()

		while self.settings.active:
			self.show_menus()
			self.check_option_user(char = input("Option: ").lower())   

			
if __name__ == '__main__':
	app = ContactApp()
	app.run()

