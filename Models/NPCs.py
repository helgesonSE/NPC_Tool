import random
import Data


class NPC:
    staticID = 0

    @staticmethod
    def GetNewID(): #Gets a new unique id when creating NPCs.
        NPC.staticID += 1
        return str(NPC.staticID - 1).rjust(4, '0')

class BaseNPC(NPC): #Inherits from NPC.
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
    def NPCValues(self):    #This list is used to access values via index. It matches the attribute enum from Data.py.
        return [self.id, self.name, self.description, self.hitPoints, self.guard, self.attackSkill,
                self.defenceSkill, self.armour]

    def SetValue(self, key, newValue):  #Setter for values. List is used with enum values (key) as index to get the names.
        attributes = ["id", "name", "description", "hitPoints", "guardPoints",
                      "attackSkill", "defenceSkill", "armour", "weapon"]
        attribute = attributes[key]
        if hasattr(self, attribute):
            setattr(self, attribute, newValue)

    def PrintValues(self, asMenu):  #Method to display the values (sans id) of a NPC, as a menu (with index) or not.
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

    def Attack(self, opposeRoll):   #opposeRoll is the opponents defence skill roll, entered manually.
        attackRoll = random.randint(0, 99)
        if attackRoll <= self.attackSkill and attackRoll >= opposeRoll: #In opposed rolls, the winner is the one who
            if isinstance(self, ArmedNPC):  #rolled the highest while under their skill value. We assume opposeRoll is valid.
                damageRoll = 0
                i = 0
                while i < self.weapon["damage"]:    #The value in "damage" represents the number of dice rolled.
                    diceResult = random.randint(1, 6)
                    if diceResult == 6: #The dice are exploding. A 6 lets you roll an extra die.
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

    def Defend(self, opposeRoll, incomingDamage):   #opposeRoll and incomingDamage are entered manually.
        defenceRoll = random.randint(0, 99)
        if defenceRoll <= self.defenceSkill and defenceRoll > opposeRoll:
            print(f"{self.name} blocked the attack!\n")
        else:
            i = 0
            armourRoll = 0
            while i < self.armour:
                diceResult = random.randint(1, 6)   #Armour dice work the same as the attack dice.
                if diceResult == 6:
                    i -= 1
                armourRoll += diceResult
                i += 1
            if armourRoll < incomingDamage:
                incomingDamage -= armourRoll
                self.guard -= incomingDamage    #Damage goes to guard first. In the game these are not real hit points,
                if self.guard < 0:              #but a buffer that recharges between fights. Once empty, damage bleeds over.
                    self.hitPoints += self.guard
                    self.guard = 0
                    if self.hitPoints < 1:
                        print(f"\n\n{self.name} has reached 0 hit points.\n\n") #Informs the user that the NPC is "dead",
                    else:                                                       #but they can keep using it if they want.
                        print(f"\n\n{self.name} received {incomingDamage} damage.\n\n")
            else:
                print(f"\n\n{self.name} absorbed the damage with its armor.\n\n")


class ArmedNPC(BaseNPC):    #Inherits from BaseNPC, has the weapon(dict) attribute.
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
