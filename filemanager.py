import json
from datetime import datetime
from json.decoder import JSONDecodeError
import player
import draft

filepath = "data.json"

def loadData():
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
    except (JSONDecodeError, FileNotFoundError):
        # If file is empty or doesn't exist, create a default
        # structure that unpackData can handle.
        data = {"players": {}}
        
    return unpackData(data)

def updateData(_data):
    with open(filepath, 'w') as file:
        json.dump(dictData(_data), file, indent=4)

def unpackData(_data):
    data = {}
    if "players" not in _data:
        return data
    for id_str, pdata in _data["players"].items():
        drafts = pdata.get("drafts", [])
        draftObjs = []
        for d in drafts:
            draftObjs.append(
                draft.draft(
                    name=d["name"],
                    placement=d["placement"],
                    rounds=d["rounds"],
                    wins=d["wins"]
                )
            )
        player_id = pdata["id"]
        data[player_id] = player.player(
            name=pdata["name"],
            id=pdata["id"],
            drafts=draftObjs
        )
    return data

def dictData(_data):
    data = {
        "lastOpened": datetime.now().date().isoformat(),
        "players": {_data[item].id: dictPlayer(_data[item]) for item in _data}
    }

    return data

def dictPlayer(_data):

    drafts = []
    for d in _data.drafts:
        drafts.append({
            "name": d.name,
            "placement": d.placement,
            "rounds": d.rounds,
            "wins": d.wins
        })
    
    data = {
            "id": _data.id,
            "name": _data.name,
            "drafts": drafts
        }
    return data
