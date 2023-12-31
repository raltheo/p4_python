from prettytable import PrettyTable
from mvc.controller.player import PlayerController
from mvc.utils.validate import validate_dob, int_input


def green(text):
    print("\x1b[6;30;42m" + text + "\x1b[0m")


def red(text):
    print("\x1b[6;30;41m" + text + "\x1b[0m")


class PlayerView:
    def displayPlayers(self, columns: list):
        x = PrettyTable()
        x.field_names = ["id", "nom", "prenom", "dob", "points"]
        for item in columns:
            x.add_row(item)
        print("\n")
        print(x)
        response = input("\nChoose a player id : ")
        while not int_input(response):
            print("please enter a number")
            response = input("\nChoose a player id : ")
        return response

    def menu(self):
        print("\n[1] Create Player\n[2] Delete Player\n[3] Back")
        response = input()
        while not int_input(response):
            print("please enter a number")
            response = input()
        return response

    def promtNewPlayer(self):
        print("\n")
        nom = input("Enter last name : ")
        prenom = input("Enter first name : ")
        dob = input("Enter date of birth (dd/mm/yyyy) : ")
        while not validate_dob(dob):
            print("erreur")
            dob = input("Enter date of birth (dd/mm/yyyy) : ")
        return nom, prenom, dob

    def saved(self):
        green("Player saved !")

    def error(self):
        red("An error occurred.")

    def delete(self):
        green("player deleted !")
