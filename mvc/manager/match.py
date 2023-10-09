from tinydb import TinyDB, Query, where

class MatchManager:
    def __init__(self):
        pass

    def save(self, match):
        db_match = TinyDB('db/db.json').table('match')
        self.mid = db_match.insert(match)
        db_match.update({'matchId': self.mid}, doc_ids=[self.mid])
        return self.mid
    
    def load_all_match(self, roundid: int):
        db_match = TinyDB('db/db.json').table('match')
        query = Query()
        db_matchs = db_match.search(query.roundId == roundid)
        columns = []
        for item in db_matchs:
            temp = []
            temp.append(item["matchId"])
            temp.append(item["player1"])
            temp.append(item["scores"][0])
            temp.append(item["player2"])
            temp.append(item["scores"][1])
            temp.append(item["finish"])
            columns.append(temp)
        return columns
    
    def load_match(self, mid: int):
        query = Query()
        db_match = TinyDB('db/db.json').table('match')
        matche = db_match.search(query.matchId == mid)
        return matche[0]
    
    def update_score(self, mid: int, score: list):
        query = Query()
        db_match = TinyDB('db/db.json').table('match')
        matche = db_match.search(query.matchId == mid)[0]
        matche['scores'] = score
        matche['finish'] = True
        db_match.update(matche, query.matchId == mid)