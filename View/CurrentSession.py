import json
from Models.NPCs import *
from Models.NPCs import NPC

class CurrentSession:

    def __init__(self):
        self.NPCList = self.loadNPCsToLists()
        self.actionInterfaceNPCs = []

    def loadNPCsToLists(self):
        jsonRead = open('Files/NPC_data.json', 'r', encoding='utf-8')
        jsonNPCs = json.load(jsonRead)
        jsonRead.close()

        _NPCList = []

        NPC.staticID = int(jsonNPCs["staticId"])

        for category, npc_list in jsonNPCs.items():
            for npc in npc_list:
                if category == "BaseNPC":   #Upon creation we make sure the incoming values are the correct type.
                    npcInstance = BaseNPC(  #Could use a failsafe. Also private variable signifiers are only used here.
                        npc['id'],
                        npc['name'],
                        int(npc['hitPoints']),
                        int(npc['guardPoints']),
                        int(npc['attackSkill']),
                        int(npc['defenceSkill']),
                        int(npc['armour']),
                        npc['description']
                        )
                elif category == "ArmedNPC":
                    npcInstance = ArmedNPC(
                        npc['id'],
                        npc['name'],
                        int(npc['hitPoints']),
                        int(npc['guardPoints']),
                        int(npc['attackSkill']),
                        int(npc['defenceSkill']),
                        int(npc['armour']),
                        npc['description'],
                        npc['weapon']
                    )
                else:
                    continue
                _NPCList.append(npcInstance)

        return _NPCList
