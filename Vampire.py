#get the super
from Character import Character

class Vampire(Character):
	def __init__(self): 
		super(Vampire, self):
		




# class Vampire(object):
# 	def __init__(self):
# 		self.name = "Vampire"
# 		self.health = 15
# 		self.power = 4
# 	def take_damage(self,amount_of_damage):
# 		self.health -= amount_of_damage
# 	def get_health(self):
# 		return self.health
# 	def is_alive(self):
# 		return self.health > 0
