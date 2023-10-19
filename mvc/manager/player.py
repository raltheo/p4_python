from tinydb import TinyDB, Query, where


class PlayerManager:
    def __init__(self):
        pass

    def save(self, player):
        db_player = TinyDB("db/db.json").table("player")
        try:
            verif = db_player.search(
                (where("nom") == self.nom)
                & (where("prenom") == self.prenom)
                & (where("dob") == self.dob)
            )
        except:
            verif = False
        if not verif:
            self.pid = db_player.insert(player)
            db_player.update({"id": self.pid}, doc_ids=[self.pid])
            return True

    def delete_player(self, pid):
        db_player = TinyDB("db/db.json").table("player")
        db_player.remove(where("id") == pid)

    def load_players(self):
        db_player = TinyDB("db/db.json").table("player")
        db_player_all = db_player.all()
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
        db_player = TinyDB("db/db.json").table("player")
        query = Query()
        db_player = db_player.search(query.id == pid)
        return db_player[0]

    def add_point(self, pid, point):
        db_player = TinyDB("db/db.json").table("player")
        query = Query()
        player = db_player.search(query.id == pid)[0]
        player["points"] = player["points"] + point
        db_player.update(player, query.id == pid)
