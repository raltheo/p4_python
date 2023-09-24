from mvc.controller.menu import MenuController
from mvc.view.menu import ViewMenu
from mvc.view.menu import PlayerView
from mvc.controller.player import PlayerController
from mvc.view.base import Views
from mvc.controller.base import Controllers


def main():
    viewmenu = ViewMenu()
    viewplayer = PlayerView()

    playercontroller = PlayerController()

    views = Views(viewmenu, viewplayer)
    controllers = Controllers(playercontroller)

    menucontroller = MenuController(views, controllers)
    menucontroller.mainStart()


if __name__ == '__main__':
    main()
