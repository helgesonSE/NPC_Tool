class UnarmedNPC:
    def __init__(self, name, hitPoints, guard,
                 attackSkill, defenceSkill,
                 armour, description):
        self.name = name
        self.hitPoints = hitPoints
        self.guard = guard
        self.attackSkill = attackSkill
        self.defenceSkill = defenceSkill
        self.armour = armour
        self.description = description





class ArmedNPC(UnarmedNPC):
    def __init__(self, name, hitPoints, guard,
                attackSkill, defenceSkill,
                armour, description, weapon):
        super().__init__(name, hitPoints, guard, attackSkill,
                        defenceSkill, armour, description)
        self.weapon = weapon
