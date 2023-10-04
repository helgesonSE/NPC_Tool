class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damageDice = damage

    def UseWeapon(self):
        import random
        _i = 0
        _totalDamage = 0

        while _i < self.damageDice + 1:
            _diceValue = random.randint(1, 6)
            if _diceValue == 6:
                _i -= 1
            _totalDamage += _diceValue

        return _totalDamage
