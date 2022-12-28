import textwrap

def wrap(string, max_width):
    output = ''''''
    for i in range(len(string)):
        output+=string[i]
        if not (i+1)%max_width:
            output+='''
'''
    return output

if __name__ == '__main__':
