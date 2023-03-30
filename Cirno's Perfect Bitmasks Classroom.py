t = int(input())

for _ in range(t):

    x = int(input())

    count = bin(x).count('1')
    least_sig_ind = (x&-x).bit_length() - 1

    y = 1<<least_sig_ind
    
    if count == 1 and not least_sig_ind:    
        y |= 2
    
    elif count == 1:
        y |= 1
    
    print(y)

    
