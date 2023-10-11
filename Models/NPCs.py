class NPC:
    staticID = 0

class BaseNPC(NPC):
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
        self.NPCKeys = ["Name: ", "Description: ", "Hit Points: ", "Guard Points: ",
                        "Attack Skill: ", "Defence Skill: ", "Armour: "]
        self.NPCValues = [self.name, self.description, self.hitPoints, self.guard, self.attackSkill,
                          self.defenceSkill, self.armour]

    def PrintValues(self, asMenu):

        i = 0
        while i < len(self.NPCKeys):
            x = ""
            if asMenu:
                x = f"[{i+1}] "
            if i == 7 and isinstance(self, ArmedNPC):
                print(x + self.NPCKeys[i].rjust(16, ' ') + self.weapon["name"] + "/ " + str(self.weapon["damage"]))
                break
            print(x + self.NPCKeys[i].rjust(16, ' ') + self.NPCValues[i])
            i += 1

class ArmedNPC(BaseNPC):
    def __init__(self, id, name, hitPoints, guardPoints,
                 attackSkill, defenceSkill,
                 armour, description, weapon):
        super().__init__(id, name, hitPoints, guardPoints, attackSkill,
                         defenceSkill, armour, description)
        self.weapon = weapon
        self.NPCKeys = ["Name: ", "Description: ", "Hit Points: ", "Guard Points: ",
                        "Attack Skill: ", "Defence Skill: ", "Armour: ", "Weapon/ Damage: "]
        self.NPCValues = [self.name, self.description, self.hitPoints, self.guard, self.attackSkill,
                          self.defenceSkill, self.armour, self.weapon]
