from mvc.model.player import Player
import datetime
regex = datetime.datetime.strptime

class PlayerController:
    @staticmethod
    def ChoosePlayer():
        players = Player.LoadPlayers()
        columns = []
        for item in players:
            temp = []
            temp.append(item["id"])
            temp.append(item["nom"])
            temp.append(item["prenom"])
            temp.append(item["dob"])
            columns.append(temp)
        from mvc.view.player import PlayerView
        PlayerView.DisplayPlayers(columns)
    
    def create(self, nom, prenom, dob):
        
        player = Player(nom, prenom, dob)
        player.save()

    @staticmethod
    def delete(pid):
        Player.deletePlayer(pid)