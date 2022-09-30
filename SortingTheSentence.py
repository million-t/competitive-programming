class Solution:
    def sortSentence(self, s: str) -> str:
        wordsList = s.split()
        sortedList = ['']*len(wordsList)
        for word in wordsList:
            sortedWordIndex = int(word[len(word) - 1]) - 1
            sortedList[sortedWordIndex] = word[:len(word)-1]
        sortedSentence = ' '.join(sortedList)
        return sortedSentence
