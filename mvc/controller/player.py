from mvc.model.player import Player
import re


class PlayerController:
    def create(self, nom, prenom, dob):
        player = Player(nom, prenom, dob)
        player.save()
        return True

    def delete(self, pid):
        try:
            players = Player.LoadPlayers()
            Player.deletePlayer(int(pid))
            playersafter = Player.LoadPlayers()
            if len(players) > len(playersafter):
                return True
            else:
                return False
        except:
            return False
