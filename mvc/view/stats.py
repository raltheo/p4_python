from prettytable import PrettyTable
from mvc.utils.validate import validate_dob, int_input


class ViewStats:
    def __init__(self):
        pass

    def menu(self):
        print("\n[1] all players by alphabetic order")
        print("[2] display all tournament")
        print("[3] display info for a specific tournament")
        print("[4] all players form a tournament")
        print("[5] show all rounds and match from a tournament")
        response = input()
        while not int_input(response):
            print("please enter a number")
            response = input()
        return response

    def player_alphabetic(self, columns):
        x = PrettyTable()
        x.field_names = ["id", "nom", "prenom", "dob", "points"]
        for item in columns:
            x.add_row(item)
        print("\n")
        print(x)

    def all_tournament(self, columns):
        x = PrettyTable()
        x.field_names = ["id", "nom", "location", "description", "start", "end"]
        for item in columns:
            x.add_row(item)
        print("\n")
        print(x)

    def tournament(self):
        response = input("enter tournois id :")
        while not int_input(response):
            print("please enter a number")
            response = input()
        return response

    def one_tournament(self, columns):
        x = PrettyTable()
        x.field_names = ["id", "nom", "location", "start", "end"]
        x.add_row(columns)
        print("\n")
        print(x)

    def all_player_tournament(self, columns: list):
        x = PrettyTable()
        x.field_names = ["id", "nom", "prenom", "dob", "points"]
        for item in columns:
            x.add_row(item)
        print("\n")
        print(x)

    def rounds(self, columns: list):
        x = PrettyTable()
        x.field_names = ["id", "nom", "start", "end", "finish"]
        x.add_row(columns)
        print("")
        print(x)

    def match(self, columns: list):
        x = PrettyTable()
        x.field_names = [
            "id",
            "player1",
            "score player1",
            "player2",
            "score player2",
            "finish",
        ]
        for item in columns:
            x.add_row(item)
        print("")
        print(x)
