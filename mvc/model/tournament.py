from tinydb import TinyDB, Query, where


class Tournament:
    def __init__(self, name: str, location: str, description: str, players: list, start_date: str = 0, end_date: str = 0, rounds: list = [], current_round: int = 0, round_total: int = 4, tid: int = 0):
        self.tid = tid
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.round_total = round_total
        self.current_round = current_round
        self.rounds = rounds
        self.players = players
        self.description = description
        self.db_tournament = TinyDB('db/db.json').table('tournament')

    def Save(self):
        self.tid = self.db_tournament.insert({
            "id": self.tid,
            "nom": self.name,
            "location": self.location,
            "start": self.start_date,
            "end": self.end_date,
            "round_total": self.round_total,
            "rounds": self.rounds,
            "players": self.players,
            "description": self.description
        })
        self.db_tournament.update({'id': self.tid}, doc_ids=[self.tid])

    def NewRound(self, round: list):
        print("test")

    @staticmethod
    def LoadTournament():
        db_tournament = TinyDB('db/db.json').table('tournament').all()
        return db_tournament
