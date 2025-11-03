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
        choice1 = input("\n============\n\n1) Get bracket\n2) List players\n3) Get ID\n4) Add draft\n5) Add player\n6) Remove player\n7) Exit\n\n============\n\n")
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
                                if checkID(data, id):
                                    players.append(data[id])
                        case "2":
                            print("\nEnter names:\n")
                            while True:
                                name = input("")
                                if name == "":
                                    break
                                data, id = getIDByName(data, name)
                                if id is not None:
                                    players.append(data[id])
                        case "3":
                            break
                        case _:
                            continue
                    order = sorted(players, key=lambda x: x.getScore(), reverse=True)
                    
                    print("\nBracket:\n")
                    for i in range(0, len(order)):
                        print(f"{i + 1}) {order[i].name} (Score: {order[i].getScore()})")
                    # bye = False
                    # num_players = len(order)
                    # if order.__len__() % 2 != 0:
                    #     bye = True
                    #     bye_player = order[-1]
                    #     num_players -= 1
                    # for i in range(0, num_players, 2):
                    #     p1 = order[i]
                    #     p2 = order[order.__len__() - 1 - i]
                    #     print(f"{p1.name} (Score: {p1.getScore():.3f}) vs {p2.name} (Score: {p2.getScore():.3f})")
                    # if bye:
                    #     print(f"{bye_player.name} gets a BYE")
                    # break
            case "2":
                sortData = dict(sorted(data.items(), key=lambda item: item[1].getScore(), reverse=True))
                for item in sortData:
                    print(f"ID: {sortData[item].id} | Name: {sortData[item].name} | Score: {round(sortData[item].getScore(), 3)}")
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
                                if checkID(data, id):
                                    ids.append(id)
                        case "2":
                            print("\nEnter names:\n")
                            while True:
                                name = input("")
                                if name == "":
                                    break
                                data, id = getIDByName(data, name)
                                if id is not None:
                                    ids.append(id)
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
                id = inputInt("\nEnter player id: ")
                os.system('cls' if os.name == 'nt' else 'clear')
                name = data[int(id)].name
                data = removePlayer(data, id)
                print(f"\nRemoved player {name} with ID {id}.\n")
            case "7":
                break
            case _:
                pass
    filemanager.updateData(data)