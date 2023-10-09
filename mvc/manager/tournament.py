from tinydb import TinyDB, Query, where


class ManageTournament:
    def __init__(self):
        pass

    def save(self, tournament):
        tournament_table = TinyDB('db/db.json').table('tournament')
        self.tid = tournament_table.insert(tournament)
        tournament_table.update({'id': self.tid}, doc_ids=[self.tid])
        return self.tid

    def add_round(self, tid, roundid: int):
        tournament_table = TinyDB('db/db.json').table('tournament')
        query = Query()
        tournament = tournament_table.get(query.id == tid)
        tournament['rounds'].append(roundid)
        tournament_table.update(tournament, query.id == tid)

    def manage_point(self, tid, pid, score):
        tournament_table = TinyDB('db/db.json').table('tournament')
        query = Query()
        tournament = tournament_table.get(query.id == tid)
        if tournament:
            for player in tournament['players']:
                if player['userid'] == pid:
                    if score == "win":
                        player['points'] = player['points'] + 1
                    elif score == "null":
                        player['points'] = player['points'] + 0.5
        tournament_table.update(tournament, query.id == tid)

    def delete_tournament(self, tid):
        tournament_table = TinyDB('db/db.json').table('tournament')
        tournament_table.remove(where('id') == tid)

    def load_all_tournament(self):
        tournament_table = TinyDB('db/db.json').table('tournament')
        db_tournament = tournament_table.all()
        columns = []
        for item in db_tournament:
            temp = []
            temp.append(item["id"])
            temp.append(item["nom"])
            temp.append(item["location"])
            temp.append(item["description"])
            temp.append(item["start"])
            temp.append(item["end"])
            columns.append(temp)
        return columns

    def load_tournament(self, tid):
        tournament_table = TinyDB('db/db.json').table('tournament')
        query = Query()
        db_tournament = tournament_table.search(query.id == tid)
        return db_tournament[0]
