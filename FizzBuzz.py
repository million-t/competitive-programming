class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        myList = []
        for i in range(1,n+1):
            item = ''
            if i%3 != 0 and i%5 != 0:
                item += str(i)
            else:
                if i%3 == 0:
                    item += 'Fizz'
                if i%5 == 0:
                    item += 'Buzz'
            myList.append(item)
        return myList
