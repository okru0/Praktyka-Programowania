class TennisGame2:
    SCORE_NAMES = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

    def __init__(self, p1_name, p2_name):
        self.p1_name = p1_name
        self.p2_name = p2_name
        self.p1_points = 0
        self.p2_points = 0

    def won_point(self, player_name):
        if player_name == self.p1_name:
            self.p1_score()
        else:
            self.p2_score()

    def score(self):
        if self.p1_points == self.p2_points:
            return self._even_score()
        if self.p1_points >= 4 or self.p2_points >= 4:
            return self._endgame_score()
        return self._regular_score()

    def _even_score(self):
        if self.p1_points < 3:
            return f"{self.SCORE_NAMES[self.p1_points]}-All"
        return "Deuce"

    def _endgame_score(self):
        point_diff = self.p1_points - self.p2_points
        if point_diff == 1:
            return f"Advantage {self.p1_name}"
        if point_diff == -1:
            return f"Advantage {self.p2_name}"
        if point_diff >= 2:
            return f"Win for {self.p1_name}"
        if point_diff <= -2:
            return f"Win for {self.p2_name}"

    def _regular_score(self):
        p1_score_name = self.SCORE_NAMES[self.p1_points]
        p2_score_name = self.SCORE_NAMES[self.p2_points]
        return f"{p1_score_name}-{p2_score_name}"

    def set_p1_score(self, number):
        for i in range(number):
            self.p1_score()

    def set_p2_score(self, number):
        for i in range(number):
            self.p2_score()

    def p1_score(self):
        self.p1_points += 1

    def p2_score(self):
        self.p2_points += 1