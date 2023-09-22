from mvc.view.player import PlayerView

class ViewMenu:
    @staticmethod
    def Banner():
        print(r"""
    
                                                       .::.
                                            _()_       _::_
                                  _O      _/____\_   _/____\_
           _  _  _     ^^__      / //\    \      /   \      /
          | || || |   /  - \_   {     }    \____/     \____/
          |_______| <|    __<    \___/     (____)     (____)
    _     \__ ___ / <|    \      (___)      |  |       |  |
   (_)     |___|_|  <|     \      |_|       |__|       |__|
  (___)    |_|___|  <|______\    /   \     /    \     /    \
  _|_|_    |___|_|   _|____|_   (_____)   (______)   (______)
 (_____)  (_______) (________) (_______) (________) (________)
 /_____\  /_______\ /________\ /_______\ /________\ /________\

""")
    @staticmethod
    def begin():
        ViewMenu.Banner()
        print("1 Create Tournament\n2 Manage Player\n3 View Some Stats")
        try:
            response = int(input())
        except: 
            print("please put a number")
        if response == 1:
            print("pas encore fais")
        elif response == 2:
            PlayerView().menu()
        elif response == 3:
            print("pas encore fais")
        else:
            print("please choose a good number")