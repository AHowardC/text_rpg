


class Tonic(object):
	cost = 5
	name = 'tonic'
	def apply(self, character):
		character.health += 2
		print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
	cost = 10
	name = 'sword'
	def apply(self, hero):
		hero.power += 2
		print "%s's power increased to %d." % (hero.name, hero.power)

class SuperTonic(object):
	cost = 7
	name = 'supertonic'
	def apply(self, character):
		character.health += 10
		print "%s's health increased to %d." % (character.name, character.health)

#buggy
class Armor(object):
	cost = 3
	name = 'armor'
	def apply(self, character):
		character.armor_points += 2
		print "%s's health increased to %d." % (character.name, character.health)





class Shopping(object):
	# If you define a variable in the scope of a class:
	# This is a class variable and you can access it like
	# Shopping.items => [Tonic, Sword]

	items = [Tonic, Sword, SuperTonic, Armor]
	def do_shopping(self, hero):
		while True:
			print "====================="
			print "Welcome to the store!"
			print "====================="
			print "You have %d coins." % hero.coins
			print "What do you want to do?"
			for i in xrange(len(Shopping.items)):
				item = Shopping.items[i]
				print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
			print "10. leave"
			input = int(raw_input("> "))
			if input == 10:
				break
			else:
				ItemToBuy = Shopping.items[input - 1]
				item = ItemToBuy()
				hero.buy(item)


