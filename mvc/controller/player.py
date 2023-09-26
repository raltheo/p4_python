from mvc.model.player import Player
import re


class PlayerController:
    def create(self, nom, prenom, dob):
        dob_pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        if re.match(dob_pattern, dob):
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
