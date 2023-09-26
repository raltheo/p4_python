from mvc.view.menu import ViewMenu
from mvc.view.player import PlayerView
from mvc.controller.player import PlayerController
from mvc.model.player import Player
import os


class MenuController:
    def __init__(self, views, controllers):
        self.views = views
        self.controllers = controllers

    def mainStart(self):
        self.views.viewmenu.Banner()
        self.mainMenu()

    def mainMenu(self):
        response = self.views.viewmenu.begin()
        if response == "1":
            print("pas encore fais")
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
            players = Player.LoadPlayers()
            response = self.views.viewplayer.displayPlayers(players)
            ok = self.controllers.playercontroller.delete(response)
            if ok:
                self.views.viewplayer.delete()
            else:
                self.views.viewplayer.error()
