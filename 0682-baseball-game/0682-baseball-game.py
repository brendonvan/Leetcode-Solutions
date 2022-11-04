class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scoreboard = []
        for i, score in enumerate(operations):
            if score == "C":
                scoreboard.pop()
            elif score == "D":
                scoreboard.append(scoreboard[-1] * 2)
            elif score == "+":
                scoreboard.append(scoreboard[-1] + scoreboard[-2])
            else:
                scoreboard.append(int(score))
        
        total_score = 0
        for score in scoreboard:
            total_score += score
            
        return total_score