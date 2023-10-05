class UnarmedNPC:
    def __init__(self, id, name, hitPoints, guard,
                 attackSkill, defenceSkill,
                 armour, description):
        self.id = id
        self.name = name
        self.hitPoints = hitPoints
        self.guard = guard
        self.attackSkill = attackSkill
        self.defenceSkill = defenceSkill
        self.armour = armour
        self.description = description


class ArmedNPC(UnarmedNPC):
    def __init__(self, id, name, hitPoints, guard,
                attackSkill, defenceSkill,
                armour, description, weapon):
        super().__init__(id, name, hitPoints, guard, attackSkill,
                        defenceSkill, armour, description)
        self.weapon = weapon