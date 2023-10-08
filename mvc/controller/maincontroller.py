from mvc.controller.menu import MenuController
from mvc.controller.base import Controllers
from mvc.controller.player import PlayerController
from mvc.controller.tournament import TournamentController

from mvc.view.menu import ViewMenu
from mvc.view.menu import PlayerView
from mvc.view.base import Views
from mvc.view.tournament import TournamentView

from mvc.manager.player import PlayerManager
from mvc.manager.base import Managers



class MainController:
    def __init__(self):
        pass

    def start(self):
        viewmenu = ViewMenu()
        viewplayer = PlayerView()
        viewtournament = TournamentView()

        playercontroller = PlayerController()
        tournamentcontroller = TournamentController()

        playermanager = PlayerManager()

        views = Views(viewmenu, viewplayer, viewtournament)
        controllers = Controllers(playercontroller, tournamentcontroller)
        manager = Managers(playermanager)

        menucontroller = MenuController(views, controllers, manager)
        menucontroller.mainStart()

