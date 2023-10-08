from tinydb import TinyDB, Query, where
from datetime import datetime

class Tournament:
    def __init__(self, name: str, location: str, description: str, players: list, round_total: int = 4):
        self.name = name
        self.location = location
        self.round_total = round_total
        self.players = players
        self.description = description

    def serialize(self):
        now = datetime.now()
        formatted_date = now.strftime("%d-%m-%Y-%H-%M")
        return {
            "id": 0,
            "nom": self.name,
            "location": self.location,
            "start": formatted_date,
            "end": "after",
            "round_total": self.round_total,
            "rounds": [],
            "players": self.players,
            "description": self.description
        }
    
    

    

    
