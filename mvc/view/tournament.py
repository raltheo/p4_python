from prettytable import PrettyTable
from mvc.utils.validate import validate_player_tournament, int_input


def green(text):
    print("\x1b[6;30;42m" + text + "\x1b[0m")


def red(text):
    print("\x1b[6;30;41m" + text + "\x1b[0m")


class TournamentView:
    def __init__(self):
        pass

    def menu(self):
        print("\n[1] Create Tournament\n[2] Continue Tournament\n[3] Back")
        response = input()
        while not int_input(response):
            print("please enter a number")
            response = input()
        return response

    def create_tournament(self, columns: list):
        x = PrettyTable()
        x.field_names = ["id", "nom", "prenom", "dob", "points"]
        id_list = []
        for item in columns:
            x.add_row(item)
            id_list.append(item[0])
        print("\n")
        print(x)
        players_id = input("\nChoose players id (ex : 1 2 3 8 5 6): ")
        input_id = players_id.split(" ")
        valid_player, message = validate_player_tournament(id_list, input_id)
        while not valid_player:
            red(message)
            players_id = input("\nChoose players id (ex : 1 2 3 8 5 6): ")
            input_id = players_id.split(" ")
            valid_player, message = validate_player_tournament(id_list, input_id)

        name = input("Name :")
        location = input("Localisation :")
        description = input("Description :")
        rounds = input("number of rounds (leave blank for default (4) ) :")
        return players_id, name, location, description, rounds

    def error(self):
        red("une erreur est survenue")

    def first_round(self):
        green(
            "Tournament and First round saved, go to continue"
            + "tournament to see match, enter results and generate next round"
        )

    def resume(self, columns: list):
        x = PrettyTable()
        x.field_names = ["id", "nom", "location", "description", "start", "end"]
        for item in columns:
            x.add_row(item)
        print("\n")
        print(x)
        print("[back] return menu")
        tournament_id = input("\nChoose tournament id: ")
        while not int_input(tournament_id):
            print("please enter number or back")
            tournament_id = input("\nChoose tournament id: ")
        return tournament_id

    def rounds(self, columns: list):
        x = PrettyTable()
        x.field_names = ["id", "nom", "start", "end", "finish"]
        for item in columns:
            x.add_row(item)
        print("\n")
        print(x)
        print("[0] Create new round")
        print("[back] return menu")
        round_id = input("\nChoose round id: ")
        while not int_input(round_id):
            print("please enter number or back")
            round_id = input("\nChoose round id: ")
        return round_id

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
        print("\n")
        print(x)
        print("[0] back")
        round_id = input("\nChoose match id for update result: ")
        while not int_input(round_id):
            print("please enter a number")
            round_id = input("\nChoose match id for update result: ")
        return round_id

    def update_score(self, player1, player2):
        print("\n")
        print(f"[1] player1 ({player1}) win")
        print(f"[2] player2 ({player2}) win")
        print("[3] match null")
        print("[4] back")
        response = input()
        while not int_input(response):
            print("please enter a number")
            response = input()
        return response

    def match_saved(self):
        green("Match result saved !")

    def round_saved(self):
        green("Round saved !")

    def new_round(self):
        name = input("\nEnter round name :")
        return name
