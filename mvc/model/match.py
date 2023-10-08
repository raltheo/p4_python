from datetime import datetime

class Match: 
    def __init__(self, roundId: int, player1: int, player2: int, scores: list):
        self.roundId = roundId
        self.player1 = player1
        self.player2 = player2
        self.scores = scores


    def serialize(self):
        
        return {
            "matchId": 0,
            "roundId": self.roundId,
            "player1": self.player1,
            "player2": self.player2,
            "scores": self.scores,
            "finish": False
        }
