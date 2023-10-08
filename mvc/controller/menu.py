from mvc.view.menu import ViewMenu
from mvc.view.player import PlayerView

from mvc.controller.player import PlayerController

from mvc.model.player import Player

import os


class MenuController:
    def __init__(self, views, controllers, manager):
        self.views = views
        self.controllers = controllers
        self.manager = manager

    def mainStart(self):
        self.views.viewmenu.Banner()
        self.mainMenu()

    def mainMenu(self):
        response = self.views.viewmenu.begin()
        if response == "1":
            self.tournament_menu()
            self.mainMenu()
        if response == "2":
            self.playerMenu()
            self.mainMenu()
        if response == "3":
            print("pas encore fais")

    def playerMenu(self):
        response = self.views.viewplayer.menu()
        if response == "1":
            nom, prenom, dob = self.views.viewplayer.promtNewPlayer()
            ok = self.controllers.playercontroller.create(nom, prenom, dob)
            if ok:
                self.views.viewplayer.saved()
            else:
                self.views.viewplayer.error()

        if response == "2":
            players = self.manager.playermanager.load_players()
            response = self.views.viewplayer.displayPlayers(players)
            ok = self.controllers.playercontroller.delete(response)
            if ok:
                self.views.viewplayer.delete()
            else:
                self.views.viewplayer.error()

    def tournament_menu(self):
        response = self.views.viewtournament.menu()
        if response == "1":
            players = self.manager.playermanager.load_players()
            players_id, name, location, description, rounds = self.views.viewtournament.create_tournament(players)
            tid = self.controllers.tournamentcontroller.create_tournament(players_id, name, location, description, rounds)
            if tid:
                roundname = self.views.viewtournament.new_round()
                ok = self.controllers.tournamentcontroller.create_first_round(tid, roundname)
                if ok:
                    self.views.viewtournament.first_round()
            else:
                self.views.viewtournament.error()
            