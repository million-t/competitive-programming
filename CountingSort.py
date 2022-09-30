def countingSort(arr):
    freqArr = [0]*100
    for i in range(len(arr)):
        freqArr[arr[i]] += 1
    return freqArr
