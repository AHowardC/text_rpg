class Hero(Character):
    def __init__(self):
        self.name = 'hero'
        self.health = 10
        self.power = 5
        self.coins = 20

    def restore(self):
        self.health = 10
        print "Hero's heath is restored to %d!" % self.health
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)


class Medic(Character):
    def __init__(self):
        self.name = 'Medic'
        self.health = 10
        self.power = 5
        self.coins = 20
    """docstring for Medic"Character d
    def __init__(self):
    self.name = 'Medic'
    self.health = 10
    self.power = 15
    self.coins = 20f __init__(self, arg):
        super(Medic,Character._
        def __init__(self):
        self.name = 'Medic'
        self.health = 10
        self.power = 15
        self.coins = 20init__()
        self.arg = arg
        