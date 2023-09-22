from tinydb import TinyDB, Query, where

class Player:

    def __init__(self, nom: str, prenom: str, dob: str, pid: int = 0):
        self.pid = pid
        self.nom = nom
        self.prenom = prenom
        self.dob = dob
        self.db_player = TinyDB('db/db.json').table('player')
    
    def Save(self):
        verif = self.db_player.search((where('nom') == self.nom) & (where('prenom') == self.prenom) & (where('dob') == self.dob))
        if not verif:
            self.pid = self.db_player.insert({"id": self.pid, "nom": self.nom, "prenom": self.prenom, "dob": self.dob, "win": 0})
            self.db_player.update({'id': self.pid}, doc_ids=[self.pid])
            return True
    
    @staticmethod
    def deletePlayer(pid):
        db_player = TinyDB('db/db.json').table('player')
        db_player.remove(where('id') == pid)
        print(db_player.all())


    @staticmethod
    def LoadPlayers():
        db_player = TinyDB('db/db.json').table('player').all()
        return db_player


