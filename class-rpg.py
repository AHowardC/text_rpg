import time 

from character import Character
from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
from wizard import Wizard
from medic import Medic 
from Shadow import Shadow
from Battle import Battle
from random import randint
from Shopping import Shopping, Tonic, Sword, SuperTonic
# from characters import Hero, Goblin

# instantiate a hero object from the Hero class
the_hero = Hero()
# ditto
# a_goblin = Goblin()
battle = Battle()
shop = Shopping()
# Make a list to hold all our monsters
monsters = []

# Before the game starts, let's ask the hero for his or her name.
print "What is thy name, brave adventurer?"
the_hero.name = raw_input("> ")
the_hero.cheer_for_hero("Good Luck Hero!")

print "How many monsters are you will to fight, brave %s?" % the_hero.name
number_of_enemies = int(raw_input("> "))

for i in range(0,number_of_enemies):
	rand_num = randint(0,2)
	if(rand_num == 1):
		monsters.append(Goblin())
	else:
		monsters.append(Vampire())
	# else:
	# 	monsters.append(Wizard())


# we need to loop through all the monsters!
for i,monster in enumerate(monsters):
	if battle.do_battle(the_hero,monster) == True:
		print "it works"
		shop.do_shopping(the_hero)
	# Run the game as long as BOTH characters have health (are alive)
	# while monster.alive() and the_hero.alive():
	# 	# game is on!
	# 	# os.system("clear")
	# 	print "You have %d health and %d power." % (the_hero.health, the_hero.power)
	# 	print "The %s has %d health and %d power." % (monster.name, monster.health, monster.power)
	# 	print "What do you want to do?"
	# 	print "1. fight %s" % monster.name
	# 	print "2. do nothing"
	# 	print "3. flee"
	# 	print "> "
	# 	user_input = raw_input()
	# 	if user_input == "1":
	# 		# User has chosen to attack. 
	# 		# Take away health from the goblin based on hero power
	# 		# goblin_health -= hero_power
	# 		# the goblin class should be managing the goblins health
	# 		# the hero is going to do the_hero.power damage to the goblin
	# 		monster.recieve_damage(the_hero.power)

	# 	elif user_input == "2":
	# 		# Hero is going to stand there like an idiot
	# 		pass
	# 	elif user_input == "3":
	# 		print "Goodbye, coward! You remind me of Goober."
	# 		os.system("say Goodbye, coward! You remind me of Goober.")
	# 		# call break, to end the while loop
	# 		break
	# 	else:
	# 		print "Invalid input %s" % user_input

	# 	# goblins turn to attack!! (only if he's still alive)
	# 	if monster.get_health() > 0:
	# 		# just like the goblin, the hero should be changing its own stuff
	# 		# so... call recieve_damage on the hero
	# 		# hero_health -= goblin_power
	# 		the_hero.recieve_damage(monster.power)

	# 		print "The %s hits you for %d damage" % (monster.name, monster.power)
	# 		# goblin has attacked, now check to see if hero is still alive...
	# 		if the_hero.alive():
	# 			print "You have been killed by the weak goblin. Shame on you."





