from tinydb import TinyDB, Query, where
from datetime import datetime


class RoundManager:
    def __init__(self):
        pass

    def save(self, round):
        db_round = TinyDB("db/db.json").table("round")
        self.rid = db_round.insert(round)
        db_round.update({"roundId": self.rid}, doc_ids=[self.rid])
        return self.rid

    def load_round(self, rid):
        query = Query()
        db_round = TinyDB("db/db.json").table("round")
        db_round = db_round.search(query.roundId == rid)
        return db_round[0]

    def load_all_round(self, tid):
        query = Query()
        db_round = TinyDB("db/db.json").table("round")
        db_rounds = db_round.search(query.tournoisId == tid)
        columns = []
        for item in db_rounds:
            temp = []
            temp.append(item["roundId"])
            temp.append(item["name"])
            temp.append(item["start"])
            temp.append(item["end"])
            temp.append(item["finish"])
            columns.append(temp)
        return columns

    def finish_round(self, rid):
        now = datetime.now()
        formatted_date = now.strftime("%d-%m-%Y-%H-%M")
        query = Query()
        db_round = TinyDB("db/db.json").table("round")
        round = db_round.search(query.roundId == rid)[0]
        round["finish"] = True
        round["end"] = formatted_date
        db_round.update(round, query.roundId == rid)
