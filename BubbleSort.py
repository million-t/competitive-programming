def countSwaps(a):
    numSwaps = 0
    for i in range(len(a)-1):
        isSorted = True
        for j in range(len(a)-i-1):
            if a[j]> a[j+1]:
                isSorted = False
                a[j], a[j+1] = a[j+1], a[j]
                numSwaps += 1
        if isSorted:
            break
    print('Array is sorted in {} swaps.'.format(numSwaps))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[len(a)-1]))
