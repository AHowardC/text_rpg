class Person(object):
	def __init__(self, name, email, phone):
		self.name = name
		self.email = email
		self.phone = phone
		self.friends = []
		self.greeting_count += 1
		self.greeted_people = []
		self.number_unique_people = 0

	def greet(self, other_person):
		print 'Hello %s, I am %s!' % (other_person.name, self.name)
		#Add a method 2. Add a print_contact_info	
	def print_contact_info():
		print self.email, self.phone
		#Add a add_friend method
	def add_friend(self, other_person):
		self.friends.append(other_person.name)
	def num_friends(self):
		return len(self.friends)
	def number_unique_people():
		pass