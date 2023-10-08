from mvc.model.tournament import Tournament
from mvc.model.round import Round
from mvc.model.match import Match

from mvc.manager.tournament import ManageTournament
from mvc.manager.round import RoundManager
from mvc.manager.match import MatchManager

import random
class TournamentController:
    def __init__(self):
        self.tournamentmanager = ManageTournament()
        self.roundmanager = RoundManager()
        self.matchmanager = MatchManager()

    def has_duplicates(self, lst):
        seen = set()
        for item in lst:
            if item in seen:
                return True
            seen.add(item)
        return False

    def create_tournament(self, players_id, name, location, description, rounds):
        players = players_id.split()
        players = [int(player) for player in players]
        if self.has_duplicates(players):
            return False
        if len(players) % 2 is not 0:
            return False
        if not rounds:
            tournament = Tournament(name, location , description, players)
            tid = self.tournamentmanager.save(tournament.serialize())
            return tid
        else:
            tournament = Tournament(name, location , description, players, int(rounds))
            tid = self.tournamentmanager.save(tournament.serialize())
            return tid

    def create_first_round(self, tid, name):
        round = Round(tid, name)
        rid = self.roundmanager.save(round.serialize())
        self.tournamentmanager.add_round(tid=tid, roundid=rid)
        print(self.tournamentmanager.load_tournament(tid))

        players = self.tournamentmanager.load_tournament(tid)["players"]
        random.shuffle(players)
        for i in range(0, len(players), 2):
            matche = Match(rid, player1=players[i], player2=players[i+1], scores=[0, 0])
            self.matchmanager.save(matche.serialize())
        return True