from prettytable import PrettyTable
from mvc.controller.player import PlayerController


def green(text):
    print('\x1b[6;30;42m' + text + '\x1b[0m')


def red(text):
    print('\x1b[6;30;41m' + text + '\x1b[0m')


class PlayerView:

    def displayPlayers(self, columns: list):

        x = PrettyTable()
        x.field_names = ["id", "nom", "prenom", "dob", "win"]
        for item in columns:
            x.add_row(item)
        print("\nChoose an Player Id\n")
        print(x)
        response = input()
        return response

    def menu(self):
        print("\n1 Create Player\n2 Delete Player\n3 Back")
        repsonse = input()
        return repsonse

    def promtNewPlayer(self):
        print("\n")
        nom = input("enter last name : ")
        prenom = input("enter first name : ")
        dob = input("enter date of birth : ")
        return nom, prenom, dob

    def saved(self):
        green("player saved !")

    def error(self):
        red("une érreur est survenue")
