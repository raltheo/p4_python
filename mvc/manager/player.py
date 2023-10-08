from tinydb import TinyDB, Query, where


class PlayerManager:
    def __init__(self):
        self.db_player = TinyDB('db/db.json').table('player')

    def save(self, player):
        try:
            verif = self.db_player.search((where('nom') == self.nom) & (
            where('prenom') == self.prenom) & (where('dob') == self.dob))
        except:
            verif = False
        if not verif:
            self.pid = self.db_player.insert(player)
            self.db_player.update({'id': self.pid}, doc_ids=[self.pid])
            return True

    def delete_player(self, pid):
        self.db_player.remove(where('id') == pid)

    def load_players(self):
        db_player_all = self.db_player.all()
        columns = []
        for item in db_player_all:
            temp = []
            temp.append(item["id"])
            temp.append(item["nom"])
            temp.append(item["prenom"])
            temp.append(item["dob"])
            temp.append(item["points"])
            columns.append(temp)
        return columns

    def get_player(self, pid):
        query = Query()
        db_player = self.db_player.search(query.id == pid)
        return db_player[0]
