import os
import player
import filemanager

data = {}

def inputInt(prompt: str) -> int:
    id = input(prompt)
    try:
        id = int(id)
    except ValueError:
        return -1
    return int(id)

def addPlayer(_data, _name: str):
    _id = max(_data.keys(), default=0) + 1
    _data[_id] = player.player(name = _name, id = _id)
    return _data, _id

def removePlayer(_data, _id: int):
    print(_data.keys())
    if _id in _data.keys():
        print("joe")
        del _data[_id]
    return _data

def getIDByName(_data, _name: str) -> int | None:
    for item in _data:
        if _data[item].name.lower() == _name.lower():
            return _data, _data[item].id
    _data, _id = addPlayer(_data, _name)
    return _data, _id

def checkID(_data, _id: int) -> bool:
    for item in _data:
        if _data[item].id == _id:
            return True
    return False

if __name__ == "__main__":
    data = filemanager.loadData()
    
    while True:
        choice1 = input("\n============\n\n1) Get bracket\n2) List players\n3) Get ID\n4) Add draft\n5) Add player\n6) Get player\n7) Exit\n\n============\n\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        match choice1:
            case "1":
                while True:
                    choice2 = input("\n1) Enter players by id\n2) Enter players by name\n3) Exit\n")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    players = []
                    match choice2:
                        case "1":
                            print("\nEnter ids:\n")
                            while True:
                                id = inputInt("")
                                if id == -1:
                                    break
                                if checkID(data, id):
                                    players.append(data[id])
                                else:
                                    print(f"\nID {id} not found.\n")
                        case "2":
                            print("\nEnter names:\n")
                            while True:
                                name = input("")
                                if name == "":
                                    break
                                data, id = getIDByName(data, name)
                                if id is not None:
                                    players.append(data[id])
                                else:
                                    print(f"\nPlayer {name} not found.\n")
                        case "3":
                            break
                        case _:
                            continue
                    order = sorted(players, key=lambda x: x.getScore(), reverse=True)
                    
                    print("\nBracket:\n")
                    for i in range(0, len(order)):
                        print(f"{i + 1}) {order[i].name} (Score: {round(order[i].getScore(), 2)})")
                    bye = False
                    num_players = len(order)
                    total_score = 0
                    for j in order:
                        total_score += j.getScore()
                    avg = total_score/num_players
                    print("")
                    if order.__len__() % 2 != 0:
                        bye = True
                        bye_player = order.pop(0)
                        num_players -= 1
                    for i in range(0, num_players, 2):
                        p1 = order[i]
                        p2 = order[order.__len__() - 1 - i]
                        p1score = round((p1.getScore() - avg) * 2, 2)
                        p2score = round((p2.getScore() - avg) * 2, 2)
                        print(f"||  {p1.name} (Score: {p1score}) vs {p2.name} (Score: {p2score})")
                    if bye:
                        print(f"||  {bye_player.name} gets a BYE")
                    break
            case "2":
                sortData = dict(sorted(data.items(), key=lambda item: item[1].getScore(), reverse=True))
                print(f"\n{"Rank: ":<6}  |  {"ID: ":<4}  |  {"Name: ":<10}  |  {f"Score: ":<7}")
                print(f"{"------":<6}--+--{"----":<4}--+--{"----------":<10}--+--{"-------":<7}")
                for i, item in enumerate(sortData):
                    print(f"{f"{i + 1} ":<6}  |  {f"{sortData[item].id}":<4}  |  {f"{sortData[item].name}":<10}  |  {f"{round(sortData[item].getScore(), 2)}":<7}")
            case "3":
                name = input("\nEnter player name: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                data, id = getIDByName(data, name)
                if id is not None:
                    print(f"\nPlayer ID for {name}: {id}\n")
                else:
                    print(f"\nPlayer {name} not found.\n")
            case "4":

                while True:
                    choice2 = input("\n1) Enter players by id\n2) Enter players by name\n3) Exit\n")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    ids = []
                    match choice2:
                        case "1":
                            print("\nEnter ids:\n")
                            while True:
                                id = inputInt("")
                                if id == -1:
                                    break
                                if checkID(data, id):
                                    ids.append(id)
                                else:
                                    print(f"\nID {id} not found.\n")

                        case "2":
                            print("\nEnter names:\n")
                            while True:
                                name = input("")
                                if name == "":
                                    break
                                data, id = getIDByName(data, name)
                                if id is not None:
                                    ids.append(id)
                                else:
                                    print(f"\nPlayer {name} not found.\n")
                        case "3":
                            break
                        case _:
                            pass
                    draft = input("\nEnter draft name: ")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    rounds = int(input("\nEnter number of rounds: "))
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(ids)
                    for id in ids:
                        wins = int(input(f"Enter number of wins for {data[id].name}: "))
                        os.system('cls' if os.name == 'nt' else 'clear')
                        placement = int(input(f"Enter {data[id].name}'s placement: "))
                        os.system('cls' if os.name == 'nt' else 'clear')
                        data[id].addDraft(draft, wins, rounds, placement)
            case "5":
                name = input("\nEnter player name: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                data, id = addPlayer(data, name)
                print(f"\nAdded player {name} with ID {id}.\n")
            case "6":
                while True:
                    choice2 = input("\n1) Enter player by id\n2) Enter player by name\n3) Exit\n")
                    os.system('cls' if os.name == 'nt' else 'clear')
                    match choice2:
                        case "1":
                            print("\nEnter id:\n")
                            id = inputInt("")
                            if checkID(data, id):
                                print(f"{data[id].name} (Score: {round(data[id].getScore(), 2)})")
                            else:
                                print(f"\nID {id} not found.\n")
                        case "2":
                            name = input("\nEnter name:\n")
                            data, id = getIDByName(data, name)
                            if id is not None:
                                print(f"{name} (Score: {round(data[id].getScore(), 2)})")
                            else:
                                print(f"\nPlayer {name} not found.\n")
                        case "3":
                            break
                        case _:
                            continue
                                    
            case "7":
                break
            case _:
                pass
    filemanager.updateData(data)