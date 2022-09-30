def insertionSort1(n, arr):
    num = arr[n-1]
    placed = False
    i = n-1
    while not placed:
        if n <= 1:
            print(arr)
            break
        elif arr[i-1]< num or i==0:
            arr[i] = num
            placed = True
        else:
            arr[i] = arr[i-1]
            i-=1

        print(' '.join(map(str,arr)))
