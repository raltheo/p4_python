from model.player import Player
from model.tournament import Tournament
from model.round import Round
from view.players import PlayersView

class TournamentController:
    def ChoosePlayers(self):
        print("choose player")
        players = Player.LoadPlayers()
        columns = []
        for item in players:
            temp = []
            temp.append(item["id"])
            temp.append(item["nom"])
            temp.append(item["prenom"])
            temp.append(item["dob"])
            columns.append(temp)
        PlayersView.DisplayPlayers(columns)

