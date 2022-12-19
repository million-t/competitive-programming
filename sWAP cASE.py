def swap_case(s):
    ans = ''
    for l in s:
        if l.islower():
            ans+= l.upper()
        elif l.isupper():
            ans+= l.lower()
        else:
            ans+= l
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
