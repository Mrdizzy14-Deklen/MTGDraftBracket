class draft:

    name: str
    placement: int
    rounds: int
    wins: int

    def __init__(self, name: str, placement: int, rounds: int, wins: int):
        self.name = name
        self.placement = placement
        self.rounds = rounds
        self.wins = wins
    
    def getRatio(self) -> float:
        return self.wins / self.rounds if self.rounds > 0 else 0