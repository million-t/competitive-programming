def dfrnt_sizes_compare(size1, size2):
    if (size1[-1] == 'S' and size2[-1] == 'M') or \
        (size1[-1] == 'M' and size2[-1] == 'L') or \
        (size1[-1] == 'S' and size2[-1] == 'L'):

        return '<'

    return '>'

def smlr_sizes_compare(size1, size2):

    if len(size1) < len(size2):
        return '<'if size1[-1] == 'L' else '>'

    elif len(size1) > len(size2):
        return '>' if size1[-1] == 'L' else '<'

    return '='

num_tests = int(input())

for _ in range(num_tests):
    first_size, second_size = input().split(' ')

    if first_size[-1] == second_size[-1]:
        print(smlr_sizes_compare(first_size, second_size))
    
    else:
        print(dfrnt_sizes_compare(first_size, second_size))
