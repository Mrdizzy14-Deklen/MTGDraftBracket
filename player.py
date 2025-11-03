import draft
class player:

    id: int
    name: str
    drafts: list

    def __init__(self, name: str | None, id: int, drafts: list | None = None) -> None:
        self.name = name
        self.id = id
        self.drafts = drafts if drafts is not None else []
    
    ## Gets player's weighted score based on previous drafts and ratios
    def getScore(self) -> float:
        ratios = sum([draft.getRatio() for draft in self.drafts])
        draftNum = len(self.drafts)
        return ratios / draftNum if draftNum > 0 else 0.0

    ## Adds a draft's ratio to the player's record
    def addDraft(self, name, wins, rounds, placement) -> None:
        self.drafts.append(draft.draft(name, placement, rounds, wins))
