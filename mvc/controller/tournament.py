from mvc.model.tournament import Tournament
from mvc.model.round import Round
from mvc.model.match import Match

from mvc.manager.tournament import ManageTournament
from mvc.manager.round import RoundManager
from mvc.manager.match import MatchManager
from mvc.manager.player import PlayerManager

import random


class TournamentController:
    def __init__(self):
        self.tournamentmanager = ManageTournament()
        self.roundmanager = RoundManager()
        self.matchmanager = MatchManager()
        self.playermanager = PlayerManager()

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
        if len(players) % 2 != 0:
            return False
        if not rounds:
            tournament = Tournament(name, location, description, players)
            tid = self.tournamentmanager.save(tournament.serialize())
            return tid
        else:
            tournament = Tournament(name, location, description, players, int(rounds))
            tid = self.tournamentmanager.save(tournament.serialize())
            return tid

    def create_first_round(self, tid, name):
        round = Round(tid, name)
        rid = self.roundmanager.save(round.serialize())
        self.tournamentmanager.add_round(tid=tid, roundid=rid)

        players = self.tournamentmanager.load_tournament(tid)["players"]
        random.shuffle(players)
        for i in range(0, len(players), 2):
            matche = Match(
                rid, player1=players[i], player2=players[i + 1], scores=[0, 0]
            )
            self.matchmanager.save(matche.serialize())
        return True

    def manage_point(self, mid, result):
        matche = self.matchmanager.load_match(mid)
        if matche["finish"]:
            return False
        score = matche["scores"]
        player1 = matche["player1"]
        player2 = matche["player2"]
        if result == 1:
            score[0] += 1
            self.playermanager.add_point(player1, 1)
            self.matchmanager.update_score(mid, score)
        if result == 2:
            score[1] += 1
            self.playermanager.add_point(player2, 1)
            self.matchmanager.update_score(mid, score)
        if result == 3:
            score[0] += 0.5
            score[1] += 0.5
            self.playermanager.add_point(player1, 0.5)
            self.playermanager.add_point(player2, 0.5)
            self.matchmanager.update_score(mid, score)

        # check if round is finish
        matches = self.matchmanager.load_all_match(matche["roundId"])

        finish = True
        for match in matches:
            if not match[5]:
                finish = False
        if finish:
            self.roundmanager.finish_round(matche["roundId"])

        # check if tournament is finish
        tid = self.roundmanager.load_round(matche["roundId"])["tournoisId"]
        tournament = self.tournamentmanager.load_tournament(tid)
        max_round = tournament["round_total"]
        if len(tournament["rounds"]) == max_round:
            all_rounds = self.roundmanager.load_all_round(tid)
            end = True
            for round in all_rounds:
                if round[3] == "not finish":
                    end = False
            if end:
                self.tournamentmanager.finish(tid)

        return True

    def have_played_together(self, pairs, player1, player2):
        for pair in pairs:
            if player1 in pair and player2 in pair:
                return True
        return False

    def create_round(self, tid, name):
        # verifier si le dernier round est fini
        rounds = self.tournamentmanager.load_tournament(tid)["rounds"]
        max_round = self.tournamentmanager.load_tournament(tid)["round_total"]
        last_rid = rounds[len(rounds) - 1]
        last_round = self.roundmanager.load_round(last_rid)
        if not last_round["finish"]:
            return False
        # si il y'a deja le nombre max de round emepecher add round
        if len(rounds) >= max_round:
            return False
        # recuperer tout les match sous forme [[player_id, player_id], [player_id, player_id]]
        all_matche = []
        for rid in rounds:
            temp = self.matchmanager.load_all_match(rid)
            for te in temp:
                all_matche.append([te[1], te[3]])

        # recuperer la list des joueurs avec leurs points respectif et les classé par ordre de points
        match_last = self.matchmanager.load_all_match(last_rid)
        players = []
        for match in match_last:
            players.append([match[1], match[2]])
            players.append([match[3], match[4]])
        players = sorted(players, key=lambda x: x[1], reverse=True)

        # crée le round
        round = Round(tid, name)
        new_rid = self.roundmanager.save(round.serialize())
        self.tournamentmanager.add_round(tid=tid, roundid=new_rid)

        # crée les nouveau match

        while players != []:
            first = players.pop(0)
            found = False
            for second in players:
                if self.have_played_together(all_matche, first[0], second[0]):
                    continue
                players.remove(second)
                matche = Match(
                    new_rid,
                    player1=first[0],
                    player2=second[0],
                    scores=[first[1], second[1]],
                )
                self.matchmanager.save(matche.serialize())
                found = True
                break
            if not found:
                second = players.pop(0)
                matche = Match(
                    new_rid,
                    player1=first[0],
                    player2=second[0],
                    scores=[first[1], second[1]],
                )
                self.matchmanager.save(matche.serialize())

        return True
