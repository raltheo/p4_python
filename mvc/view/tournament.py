from prettytable import PrettyTable


def green(text):
    print('\x1b[6;30;42m' + text + '\x1b[0m')


def red(text):
    print('\x1b[6;30;41m' + text + '\x1b[0m')

class TournamentView: 
    def __init__(self):
        pass

    def menu(self):
        print("\n[1] Create Tournament\n[2] Continue Tournament\n[3] Back")
        repsonse = input()
        return repsonse
    
    def create_tournament(self, columns: list):
        x = PrettyTable()
        x.field_names = ["id", "nom", "prenom", "dob", "points"]
        for item in columns:
            x.add_row(item)
        print("\n")
        print(x)
        players_id = input("\nChoose players id (ex : 1 2 3 8 5 6): ")
        name = input("Name :")
        location = input("Localisation :")
        description = input("Description :")
        rounds = input("number of rounds (leave blank for default (4) ) :")
        return players_id, name, location, description, rounds
    
    def error(self):
        red("une erreur est survenue")


    def new_round(self):
        response = input("enter Round Name :")
        return response
    
    def first_round(self):
        green("Tournament and First round saved, go to continue tournament to see match, enter results and generate next round")