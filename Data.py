from enum import Enum
from View.CurrentSession import CurrentSession
class MenuOrList(Enum):
    Menu = 1
    List = 2

class Keys(Enum):
    Name = 1
    Description = 2
    HitPoints = 3
    GuardPoints = 4
    AttackSkill = 5
    DefenceSkill = 6
    Armour = 7
    Weapon = 8


session = CurrentSession()