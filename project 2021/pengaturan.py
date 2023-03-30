
class Pengaturan:

	def __init__(self):
		self.active = False
		self.contacts_location = "data/contacts.json"
		self.users_location = "data/users.json"

		self.contacts = None
		self.users = None

		self.menu = """*Barang Warung*
1. Tunjukkan Semua Barang
2. Temukan Barang 
3. Tambah Barang Baru
4. Update Barang
5. Hapus Barang
Q. Keluar
"""