
# ScoreManager.py
class ScoreManager:
    def __init__(self):
        self.scores = []
    
    def add_score(self, player, score):
        self.scores.append((player, score))
        self.scores.sort(key=lambda x: x[1], reverse=True)
    
    def show_scores(self):
        print("Mejores puntajes:")
        for i, (player, score) in enumerate(self.scores, 1):
            print(f"{i}. {player.name}: {score} puntos")
    
    def best_score(self):
        return max(self.scores, key=lambda x: x[1])[1] if self.scores else 0