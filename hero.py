class Hero:
    def __init__(self, name, hp, level, defense, damage):
        self._name = name
        self._hp = hp
        self._level = level
        self._hero_defense = defense
        self._damage = damage

    @property
    def name(self):
        return self._name

    @property
    def damage(self):
        return self._damage

    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, value):
        self._hp = value
    
    @property
    def hero_defense(self):
        return self._hero_defense

    def attack(self, target):
        print(f"{self._name} атакует {target.name}!")

    def defense(self, target):
        print(f"{self._name} отбил защиту от {target.name}")

    def dodge(self, target):
        print(f"{self._name} уклонился от {target.name}")

    def is_alive(self):
        return max(0, self._hp)

