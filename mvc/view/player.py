from prettytable import PrettyTable
from mvc.controller.player import PlayerController

class PlayerView:
    @staticmethod
    def DisplayPlayers(columns: list):
        x = PrettyTable()
        x.field_names = ["id", "nom", "prenom", "dob"]
        for item in columns:
            x.add_row(item)
        print("\n")
        print(x)


    @staticmethod
    def menu():
        print("\n\n1 Create Player\n2 Delete Player")
        try:
            response = int(input())
        except: 
            print("please put a number")
        if response == 1:
            PlayerController().create()
        elif response == 2:
            PlayerController().ChoosePlayer()
            print("choose id to delete")
            try:
                response = int(input())
                PlayerController().delete(response)
            except: 
                print("please put a number")
                
        else:
            print("please choose a good number")