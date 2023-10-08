from tinydb import TinyDB, Query, where

class RoundManager:
    def __init__(self):
        self.db_round = TinyDB('db/db.json').table('round')

    def save(self, round):
        self.rid = self.db_round.insert(round)
        self.db_round.update({'roundId': self.rid}, doc_ids=[self.rid])
        return self.rid
    
    def load_round(self, rid):
        query = Query()
        db_round = self.db_round.search(query.roundId == rid)
        return db_round[0]