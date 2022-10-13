class Hero:
    def __init__(self, name, strength, agility, intellegence):
        self.name           = name
        self.strength       = strength
        self.agility        = agility
        self.intellegence   = intellegence
        self.moveSpeed      = agility * 10
        self.maxMana        = intellegence * 10
        self.maxHealth      = strength * 10
        self.atkSpeed       = agility * 5
        self.manaRegen      = intellegence/50
        self.healthRegen    = strength/50
        self.ad             = None
        self.atkRange       = None


class Warrior(Hero):
    def __init__(self, name, strength, agility, intellegence):
        super().__init__(name, strength, agility, intellegence)
        self.ad = strength
        self.atkRange = 50

class Mage(Hero):
    def __init__(self, name, strength, agility, intellegence):
        super().__init__(name, strength, agility, intellegence)
        self.ad = intellegence
        self.atkRange = 150

class Archer(Hero):
    def __init__(self, name, strength, agility, intellegence):
        super().__init__(name, strength, agility, intellegence)
        self.ad = agility
        self.atkRange = 300

class Assassin(Hero):
    def __init__(self, name, strength, agility, intellegence):
        super().__init__(name, strength, agility, intellegence)
        self.ad = 0.5 * (agility + strength + intellegence)
        self.atkRange = 100