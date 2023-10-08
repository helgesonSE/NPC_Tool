class BaseNPC:
    staticID = 0
    def __init__(self, id, name, hitPoints, guardPoints,
                 attackSkill, defenceSkill,
                 armour, description):
        self.id = id
        self.name = name
        self.hitPoints = hitPoints
        self.guard = guardPoints
        self.attackSkill = attackSkill
        self.defenceSkill = defenceSkill
        self.armour = armour
        self.description = description

class ArmedNPC(BaseNPC):
    def __init__(self, id, name, hitPoints, guardPoints,
                 attackSkill, defenceSkill,
                 armour, description, weapon):
        super().__init__(id, name, hitPoints, guardPoints, attackSkill,
                         defenceSkill, armour, description)
        self.weapon = weapon
