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




sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
jordan = Person('Jordan','jordan@aol.com','495-586-3456')

sonny.greet(jordan.name)
jordan.greet(sonny.name)



		

		sonny.print_contact_info()
		
		

print sonny.friends
sonny.add_friend(jordan)

#Add an instance variable (attribute)
jordan.friends.append(sonny)
sonny.friends.append(jordan)

print sonny.email, sonny.phone
print jordan.email, jordan.phone


class Vehicle(object):
	def __init__(self, model, make, year):
		self.model = model
		self.make = make
		self.year = year
		#super(Vehicle, self).__init__(model, make, year	self.arg = argmodel, make, year
	def print_info(self):
		print

car = Vehicle('Nissan', 'Leaf', 2015)
print car.make, car.model, car.year



























