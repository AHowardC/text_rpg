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

class ElectricCar(Vehicle):
	def __init__(self, make, model, year, max_range, battery_size):
		super(ElectricCar,self).__init__(make, model, year,0)
		self.max_range = max_range
		self.battery_size = battery_size