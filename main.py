from ReadWriteNPCsView.Models.baseCreature import *

Bengt = UnarmedNPC("Bengt", 20, 23,
                   70, 60,
                   4, "Kraftig karl som knuffar dig med magen")

Ulfis = ArmedNPC("Ulfis", 20, 20,
                 96, 20,
                 2, "Han är en barbar!", "Kniv")

print(Ulfis.defenceSkill)
print(Ulfis.weapon + "\n" + Ulfis.weapon)

print(Bengt.name)
print(Bengt.description)











