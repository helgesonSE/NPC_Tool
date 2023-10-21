from enum import Enum
from View.CurrentSession import CurrentSession

class Attribute(Enum):  #Used to print attribute names and also access them based on index.
    Name = 1
    Description = 2
    HitPoints = 3
    GuardPoints = 4
    AttackSkill = 5
    DefenceSkill = 6
    Armour = 7
    Weapon = 8


session = CurrentSession()  #the session objects holds our lists of NPC objects and loads from file.