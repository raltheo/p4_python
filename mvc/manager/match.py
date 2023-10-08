from tinydb import TinyDB, Query, where

class MatchManager:
    def __init__(self):
        self.db_match = TinyDB('db/db.json').table('match')

    def save(self, match):
        self.mid = self.db_match.insert(match)
        self.db_match.update({'matchId': self.mid}, doc_ids=[self.mid])
        return self.mid
    
    def load_all_match(self, roundid: int):
        query = Query()
        db_match = self.db_match.search(query.roundId == roundid)
        return db_match
    
    def load_match(self, mid: int):
        query = Query()
        matche = self.db_match.search(query.matchId == mid)
        return matche[0]
    
    def update_score(self, mid: int, score: list):
        query = Query()
        matche = self.db_match.search(query.matchId == mid)[0]
        print(score)
        matche['scores'] = score
        matche['finish'] = True
        self.db_match.update(matche, query.matchId == mid)