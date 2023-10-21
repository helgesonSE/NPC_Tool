import random
import Data


class NPC:
    staticID = 0

    @staticmethod
    def GetNewID():
        NPC.staticID += 1
        return str(NPC.staticID - 1).rjust(4, '0')


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

    @property
    def NPCValues(self):
        return [self.id, self.name, self.description, self.hitPoints, self.guard, self.attackSkill,
                self.defenceSkill, self.armour]

    def SetValue(self, key, newValue):
        attributes = ["id", "name", "description", "hitPoints", "guardPoints",
                      "attackSkill", "defenceSkill", "armour", "weapon"]
        attribute = attributes[key]
        if hasattr(self, attribute):
            setattr(self, attribute, newValue)

    def PrintValues(self, asMenu):
        i = 1
        while i < len(self.NPCValues):
            x = ""
            if asMenu:
                x = f"[{i}] "
            if i == 8 and isinstance(self, ArmedNPC):
                print(x + str(Data.Attribute(i).name).rjust(16, ' ') + ": " +
                      self.weapon["name"] + "/ " + str(self.weapon["damage"]))
                break
            print(x + str(Data.Attribute(i).name).rjust(16, ' ') + ": " + str(self.NPCValues[i]))
            i += 1

    def GetID(self):
        return self.id

    def Attack(self, opposeRoll):
        attackRoll = random.randint(0, 99)
        if attackRoll <= self.attackSkill and attackRoll >= opposeRoll:
            if isinstance(self, ArmedNPC):
                damageRoll = 0
                i = 0
                while i < self.weapon["damage"]:
                    diceResult = random.randint(1, 6)
                    if diceResult == 6:
                        i -= 1
                    damageRoll += diceResult
                    i += 1
                print(f"{self.name} did {damageRoll} damage with its {self.weapon['name']}!\n")

            else:
                damageRoll = 0
                i = 0
                while i < 3:
                    diceResult = random.randint(1, 6)
                    if diceResult == 6:
                        i -= 1
                    damageRoll += diceResult
                    i += 1
                print(f"{self.name} did {damageRoll} damage with its natural attack!\n")
        else:
            print(f"{self.name} missed its attack!\n")

    def Defend(self, opposeRoll, incomingDamage):
        defenceRoll = random.randint(0, 99)
        if defenceRoll <= self.defenceSkill and defenceRoll > opposeRoll:
            print(f"{self.name} blocked the attack!\n")
        else:
            i = 0
            armourRoll = 0
            while i < self.armour:
                diceResult = random.randint(1, 6)
                if diceResult == 6:
                    i -= 1
                armourRoll += diceResult
                i += 1
            if armourRoll < incomingDamage:
                incomingDamage -= armourRoll
                self.guard -= incomingDamage
                if self.guard < 0:
                    self.hitPoints += self.guard
                    self.guard = 0
                    if self.hitPoints < 1:
                        print(f"\n\n{self.name} has reached 0 hit points.\n\n")
                    else:
                        print(f"\n\n{self.name} received {incomingDamage} damage.\n\n")
            else:
                print(f"\n\n{self.name} absorbed the damage with its armor.\n\n")


class ArmedNPC(BaseNPC):
    def __init__(self, id, name, hitPoints, guardPoints,
                 attackSkill, defenceSkill,
                 armour, description, weapon):
        super().__init__(id, name, hitPoints, guardPoints, attackSkill,
                         defenceSkill, armour, description)
        self.weapon = weapon

    @property
    def NPCValues(self):
        return [self.id, self.name, self.description, self.hitPoints, self.guard, self.attackSkill,
                self.defenceSkill, self.armour, self.weapon]
