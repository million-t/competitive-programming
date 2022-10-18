class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if not tokens: return 0
        tokens.sort()
        left, right = 0, len(tokens) - 1
        score = 0
        mxScore = 0
        while left <= right and (score or power >= tokens[left]):
            if  power >= tokens[left]:
                power-=tokens[left]
                score+=1
                left+=1
            elif score:
                score -= 1
                power += tokens[right]
                right -= 1
            else:
                break
            mxScore=max(score,mxScore)
        return mxScore
                

