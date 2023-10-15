from prettytable import PrettyTable

class ViewStats:
    def __init__(self):
        pass

    def menu(self):
        print("\n[1] all players by alphabetic order")
        print("[2] display all tournament")
        print("[3] display info for a specific tournament")
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
        return response
    
    def one_tournament(self, columns):
        x = PrettyTable()
        x.field_names = ["id", "nom", "location", "start", "end"]
        x.add_row(columns)
        print("\n")
        print(x)