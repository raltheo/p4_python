from mvc.manager.player import PlayerManager
from mvc.manager.tournament import ManageTournament
from mvc.manager.match import MatchManager
class StatsController:
    def __init__(self):
        self.playermanager = PlayerManager()
        self.tournamentmanager = ManageTournament()
        self.matchmanager = MatchManager()

    def alphabetic(self):
        data = self.playermanager.load_players()
        sorted_data = sorted(data, key=lambda x: x[1])
        return sorted_data

    def all_players(self, tid):
        pid = self.tournamentmanager.load_tournament(tid)["players"]
        players = []
        for id in pid:
            player = self.playermanager.get_player(id)
            temp = []
            temp.append(player["id"])
            temp.append(player["nom"])
            temp.append(player["prenom"])
            temp.append(player["dob"])
            temp.append(player["points"])
            players.append(temp)
        sorted_data = sorted(players, key=lambda x: x[1])
        print(sorted_data)
        return sorted_data
    
    def match_round(self, rid):
        matches = self.matchmanager.load_all_match(rid)
        for matche in matches:
            name1 = self.playermanager.get_player(matche[1])["nom"]
            prenom1 = self.playermanager.get_player(matche[1])["prenom"]
            name2 = self.playermanager.get_player(matche[3])["nom"]
            prenom2 = self.playermanager.get_player(matche[3])["prenom"]
            matche[1] = name1 + " " + prenom1
            matche[3] = name2 + " " + prenom2

        return matches