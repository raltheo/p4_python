from mvc.model.player import Player
from mvc.manager.player import PlayerManager


class PlayerController:
    def __init__(self):
        self.playermanager = PlayerManager()

    def create(self, nom, prenom, dob):
        player = Player(nom, prenom, dob)
        self.playermanager.save(player.serialize())
        return True

    def delete(self, pid):
        try:
            players = self.playermanager.load_players()
            self.playermanager.delete_player(int(pid))
            playersafter = self.playermanager.load_players()
            if len(players) > len(playersafter):
                return True
            else:
                return False
        except:
            return False
