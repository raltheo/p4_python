from mvc.manager.player import PlayerManager

class StatsController:
    def __init__(self):
        self.playermanager = PlayerManager()

    
    def alphabetic(self):
        data = self.playermanager.load_players()
        sorted_data = sorted(data, key=lambda x: x[1])
        return sorted_data
