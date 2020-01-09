class Enterprise:
	def __init__(self, name, address, phone, spec, time):
		self.name = name
		self.address = address
		self.phone = phone
		self.spec = spec
		self.time = time

	def __str__(self):
		return "{0} ({1}, {2}, {3}, {4})".format(self.name, self.address, self.phone, self.spec, self.time)

class AllEnterprises:
	def __init__(self):
		self.enterprises = []

	def load_from_file(self):
		with open("enterprises.txt") as f:
			count = int(f.readline())

			for i in range(count):
				name = f.readline().rstrip()
				address = f.readline().rstrip()
				phone = f.readline().rstrip()
				spec = f.readline().rstrip()
				time = f.readline().rstrip()

				self.enterprises.append(
					Enterprise(name, address, phone, spec, time)
				)

	def finder(self, search_by, search, item):
		if search_by == "name":
			return search in item.name
		if search_by == "phone":
			return search in item.phone
		if search_by == "spec":
			return search in item.spec
		if search_by == "address":
			return search in item.address
		if search_by == "time":
			return search in item.time
		return False


	def find_enterprise(self, search_by, search):
		return list(filter(lambda x: self.finder(search_by, search, x), self.enterprises))

db = AllEnterprises()
db.load_from_file()

search_by = input("Search criteria (name, phone, address, spec, time): ")
s = input("Search: ")
for m in db.find_enterprise(search_by, s):
	print(m)