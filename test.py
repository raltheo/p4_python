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
import itertools


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

# maxs = 4
# test = [1,1,1,1]
# print(len(test))

# print(roundmanager.load_all_round(1))


# create rounddDDDDDDDDDDDDDDDDDDDDDDDDD


def have_played_together(pairs, player1, player2):
    for pair in pairs:
        if player1 in pair and player2 in pair:
            return True
    return False


rounds = tournamentmanager.load_tournament(1)["rounds"]
last_rid = rounds[len(rounds) - 1]
last_round = roundmanager.load_round(last_rid)
if last_round["finish"] == False:
    print("pas possible round avant pas fini")
    exit()

all_matche = []
for rid in rounds:
    temp = matchmanager.load_all_match(rid)
    for te in temp:
        all_matche.append([te[1], te[3]])
print(all_matche)

match_last = matchmanager.load_all_match(last_rid)
players = []
for match in match_last:
    players.append([match[1], match[2]])
    players.append([match[3], match[4]])
players = sorted(players, key=lambda x: x[1], reverse=True)
print(players)

players_sorted = []
for player in players:
    players_sorted.append(player[0])
print(players_sorted)

new_match = []

while players != []:
    first = players.pop(0)
    print(first)
    found = False
    for second in players:
        if have_played_together(all_matche, first[0], second[0]):
            continue
        players.remove(second)
        new_match.append([first[0], second[0]])
        found = True
        break
    if not found:
        second = players_sorted.pop(0)
        new_match.append([first[0], second[0]])


print(new_match)
# matche = Match(4, player1=players[i], player2=players[i+1], scores=[0, 0])
# print(matche)

# from datetime import datetime

# # Get the current date and time
# now = datetime.now()

# # Format the datetime object as "dd-mm-yyyy-hh-mm"
# formatted_date = now.strftime("%d-%m-%Y-%H-%M")

# print(formatted_date)

# test1 = [1,1,1]
# test2 = [1,1,1,1]
# print(len(test1) % 2)
# print(len(test2) % 2)


tournois = {
    "id": 1,
    "name": "name",
    "players": [1, 2, 3, 4, 5, 6, 7, 8],
}

rounds = {
    "idRound": 1,
    "tournoId": 1,
    "name": "Round 1",
    "start": "now",
    "finish": False,
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
