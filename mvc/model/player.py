class Player:
    def __init__(self, nom: str, prenom: str, dob: str, pid: int = 0):
        self.pid = pid
        self.nom = nom
        self.prenom = prenom
        self.dob = dob

    def serialize(self):
        return {
            "id": self.pid,
            "nom": self.nom,
            "prenom": self.prenom,
            "dob": self.dob,
            "points": 0,
        }
