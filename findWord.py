def findWord(alphabetList):
    alphaDict = {}
    for i in alphabetList:
        if i[0] not in alphaDict:
            alphaDict[i[0]] = i[2]
        # elif i[0] in alphaDict:
    l = len(alphaDict)
    visited = []
    for i in alphaDict:
        temp = alphaDict[i]
        while len(visited) != l:
            visited.append(temp)
            alphaDict[i] = alphaDict[i] + alphaDict[temp]
            if alphaDict[temp] in alphaDict:
                temp = alphaDict[temp]

    return alphaDict

# def _findword()


alphabetList = ["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]

print(findWord(alphabetList))
