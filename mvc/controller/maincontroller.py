from mvc.controller.menu import MenuController
from mvc.controller.base import Controllers
from mvc.controller.player import PlayerController
from mvc.controller.tournament import TournamentController
from mvc.controller.stats import StatsController

from mvc.view.menu import ViewMenu
from mvc.view.menu import PlayerView
from mvc.view.base import Views
from mvc.view.tournament import TournamentView
from mvc.view.stats import ViewStats

from mvc.manager.player import PlayerManager
from mvc.manager.base import Managers
from mvc.manager.tournament import ManageTournament
from mvc.manager.round import RoundManager
from mvc.manager.match import MatchManager


class MainController:
    def __init__(self):
        pass

    def start(self):
        viewmenu = ViewMenu()
        viewplayer = PlayerView()
        viewtournament = TournamentView()
        viewstats = ViewStats()

        playercontroller = PlayerController()
        tournamentcontroller = TournamentController()
        statscontroller = StatsController()

        playermanager = PlayerManager()
        tournamentmanager = ManageTournament()
        roundmanager = RoundManager()
        matchmanager = MatchManager()

        views = Views(viewmenu, viewplayer, viewtournament, viewstats)
        controllers = Controllers(
            playercontroller, tournamentcontroller, statscontroller
        )
        manager = Managers(playermanager, tournamentmanager, roundmanager, matchmanager)

        menucontroller = MenuController(views, controllers, manager)
        menucontroller.mainStart()
