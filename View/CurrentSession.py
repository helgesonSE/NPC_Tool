import json
from Models.NPCs import *

class CurrentSession:
    def __init__(self):
        self.NPCList = self.loadNPCsToLists()


    def loadNPCsToLists(self):
        jsonRead = open('Files/NPC_data.json', 'r', encoding='utf-8')
        jsonNPCs = json.load(jsonRead)
        jsonRead.close()
        print(jsonNPCs)

        _NPCList = []

        NPC.staticID = int(jsonNPCs["staticId"])

        for category, npc_list in jsonNPCs.items():
            for npc in npc_list:
                if category == "BaseNPC":
                    npcInstance = BaseNPC(
                        npc['id'],
                        npc['name'],
                        npc['hitPoints'],
                        npc['guardPoints'],
                        npc['attackSkill'],
                        npc['defenceSkill'],
                        npc['armour'],
                        npc['description']
                        )
                elif category == "ArmedNPC":
                    npcInstance = ArmedNPC(
                        npc['id'],
                        npc['name'],
                        npc['hitPoints'],
                        npc['guardPoints'],
                        npc['attackSkill'],
                        npc['defenceSkill'],
                        npc['armour'],
                        npc['description'],
                        npc['weapon']
                    )
                else:
                    continue
                _NPCList.append(npcInstance)

        return _NPCList
