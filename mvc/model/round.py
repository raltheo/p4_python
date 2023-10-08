class Round:
    def __init__(self, tournoisId: int, name: str):
        self.tournoisId = tournoisId
        self.name = name
        self.start = "now"
        self.end = "after"
        self.finish = False

    def serialize(self):
        return {
            "roundId" : 0,
            "tournoisId" : self.tournoisId,
            "name" : self.name,
            "start" : self.start,
            "end" : self.end,
            "finish": self.finish
        }
