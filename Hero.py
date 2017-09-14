from character import Character
import time
class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 15
        self.power = 5
        self.coins = 20
        #trying to add armor attribute for hero and store
        self.armor = 0

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(self)

    def armor(self, item):
        self.coins -= item.cost
        item.apply(self)

    def cheer_for_hero(self, thing_to_print):
        print thing_to_print

