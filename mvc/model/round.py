from datetime import datetime


class Round:
    def __init__(self, tournoisId: int, name: str):
        self.tournoisId = tournoisId
        self.name = name
        self.start = "now"
        self.end = "after"
        self.finish = False

    def serialize(self):
        now = datetime.now()
        formatted_date = now.strftime("%d-%m-%Y-%H-%M")
        return {
            "roundId": 0,
            "tournoisId": self.tournoisId,
            "name": self.name,
            "start": formatted_date,
            "end": self.end,
            "finish": self.finish,
        }
