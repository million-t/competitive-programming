class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        
        res_student = {}
        to_be_sorted = []
        for row in score:
            key = row[k]
            res_student[key] = row
            to_be_sorted.append(key)
        
        
        to_be_sorted.sort(reverse = True)
        for ind in range(len(score)):
            score[ind] = res_student[to_be_sorted[ind]]
        
        return score
        