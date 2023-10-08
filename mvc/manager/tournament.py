from tinydb import TinyDB, Query, where


class ManageTournament:
    def __init__(self):
        self.tournament_table = TinyDB('db/db.json').table('tournament')

    def save(self, tournament):
        self.tid = self.tournament_table.insert(tournament)
        self.tournament_table.update({'id': self.tid}, doc_ids=[self.tid])
        return self.tid

    def add_round(self, tid, roundid: int):
        query = Query()
        tournament = self.tournament_table.get(query.id == tid)
        tournament['rounds'].append(roundid)
        self.tournament_table.update(tournament, query.id == tid)

    def manage_point(self, tid, pid, score):
        query = Query()
        tournament = self.tournament_table.get(query.id == tid)
        if tournament:
            for player in tournament['players']:
                if player['userid'] == pid:
                    if score == "win":
                        player['points'] = player['points'] + 1
                    elif score == "null":
                        player['points'] = player['points'] + 0.5
        self.tournament_table.update(tournament, query.id == tid)

    def delete_tournament(self, tid):
        self.tournament_table.remove(where('id') == tid)

    def load_all_tournament(self):
        db_tournament = self.tournament_table.all()
        return db_tournament

    def load_tournament(self, tid):
        query = Query()
        db_tournament = self.tournament_table.search(query.id == tid)
        return db_tournament[0]
