from mvc.model.tournament import Tournament
from mvc.model.player import Player
from mvc.model.round import Round
from mvc.model.match import Match

from mvc.manager.tournament import ManageTournament
from mvc.manager.player import PlayerManager
from mvc.manager.round import RoundManager
from mvc.manager.match import MatchManager

import random
import json

tournamentmanager = ManageTournament()
playermanager = PlayerManager()
roundmanager = RoundManager()
matchmanager = MatchManager()
# create player 
# print(playermanager.load_players())
# for i in range(8):
#     player = Player(f"test{i}",f"test{i}","20/12/2000")
#     print(player.serialize())
#     playermanager.save(player.serialize())

# print(playermanager.load_players())


# CREATE TOURNAMENT
# player = [1, 2, 3, 4, 5, 6, 7, 8]
# tournament = Tournament("oui", "paris" , "descriptions", player, "now", "after")
# tournamentmanager.save(tournament.serialize())
# print(tournamentmanager.load_all_tournament())

# CREATE ROUNDS

# FIRST ROUND

# round = Round(1, "round 1")
# print(roundmanager.save(round.serialize())) # roundId = 1 
# tournamentmanager.add_round(tid=1, roundid=1)
# print(tournamentmanager.load_tournament(1))


# create match

# first match 

# tid = 1
# roundid = 1
# print(tournamentmanager.load_tournament(1))
# players = tournamentmanager.load_tournament(1)["players"]
# random.shuffle(players)
# for i in range(0, len(players), 2):
#     matche = Match(roundid, player1=players[i], player2=players[i+1], scores=[0, 0])
#     matchmanager.save(matche.serialize())


# update scores
# print("choose tournament :")
# for i in tournamentmanager.load_all_tournament():
#     print(f"[{i['id']}] {i['nom']} {i['location']}")

# rounds = tournamentmanager.load_tournament(1)['rounds']
# print("\n")
# print("continue tournament")
# for id in rounds:
#     print(f"[{id}] {roundmanager.load_round(id)['name']}, finish : {roundmanager.load_round(id)['finish']}")

# print("\n")
# print("choose match")
# for match in matchmanager.load_all_match(1):
#     if match['finish'] is not True:
#         print(f"[{match['matchId']}] {playermanager.get_player(match['player1'])['nom']} {playermanager.get_player(match['player1'])['prenom']} vs {playermanager.get_player(match['player2'])['nom']} {playermanager.get_player(match['player2'])['prenom']}")
# id = int(input("match id : "))
# print("\nenter result")
# matche = matchmanager.load_match(id)
# print(f"[1] {playermanager.get_player(matche['player1'])['nom']} {playermanager.get_player(matche['player1'])['prenom']} win")
# print(f"[2] {playermanager.get_player(matche['player2'])['nom']} {playermanager.get_player(matche['player2'])['prenom']} win")
# print(f"[3] match null")
# reponse = int(input())

# score = matche['scores']
# if reponse == 1:
#     score[0] += 1
#     matchmanager.update_score(id, score)
# elif reponse == 2:
#     score[1] += 1
#     matchmanager.update_score(id, score)
# else:
#     score[0] += 0.5
#     score[1] += 0.5
#     matchmanager.update_score(id, score)
# print(matchmanager.load_match(id))











tournois = {
    "id": 1,
    "name": "name",
    "players": [1,2,3,4,5,6,7,8],
}

rounds = {
    "idRound" : 1,
    "tournoId": 1,
    "name" : "Round 1",
    "start": "now",
    "finish": False
}



# print(players)
# random.shuffle(players)
# matches = []
# for i in range(0, len(players), 2):
#     matches.append((players[i], players[i+1]))
# print(matches)

# CREATE ROUNDS

# FIRST ROUND
# tourois = Tournament.load_tournament(1)
# print(tourois)
# joueurs = []
# for i in tourois["players"]:
#     joueurs.append([i["userid"], i["points"]])
# random.shuffle(joueurs)
# matches = []
# for i in range(0, len(joueurs), 2):
#     matches.append((joueurs[i], joueurs[i+1]))
# print(matches)
# data = {"name": "Round 2", "start" : "now" , "end" : False, "matchs" : matches}
# tournois = ManageTournament()
# tournois.add_round(1, data)
# print(Tournament.load_tournament(1))

# ([1, 0], [2, 0])


# managerplayer = managerplayer()

# modelplayer = Modelplayer()
# modelplayer("dsfdsfds")

# managerplayer(modelplayer.serialize())


# Manage point

# tournois = ManageTournament()
# tournois.manage_point(1, 1, "win")
# tournois = Tournament.load_tournament(1)
# print(tournois["rounds"])
# print("\nenter result for round :")
# index = 0
# for round in tournois["rounds"]:
#     print(f"[{index}] {round['name']}")
#     index += 1
# reponse = int(input())

# index = 0
# if tournois["rounds"][reponse]['end'] == False:
#     for match in tournois["rounds"][reponse]["matchs"]:
#         print(f"[{index}] {Player.get_player(match[0][0])['prenom']} vs {Player.get_player(match[1][0])['prenom']}")
#         index += 1
#     print(f"[{index+1}] round finish")
#     reponse = int(input())
#     if reponse == index+1:
#         print("back")
# else:
#     print("round fini")


# for round in tourois["rounds"]:
#     while round[2] == False:
#            response = input("enter result for match :\n")


# AFTER ROUND 1

# tourois = Tournament.load_tournament(1)
# print(tourois["players"])
# joueurs = []
# for i in tourois["players"]:
#     joueurs.append([i["userid"], i["points"]])

# sorted_joueurs = sorted(joueurs, key=lambda x: x[1], reverse=True)

# print(sorted_joueurs)

# tournois = ManageTournament()
# tournois.delete_tournament(2)