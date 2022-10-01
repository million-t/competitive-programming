def countingValleys(steps, path):
    valleys = 0
    elevation = 0
    for step in path:
        elevation += (1 if step == 'U' else -1)
        if elevation == 0 and step == 'U':
            valleys+=1
    return valleys
