import os
filepath = "/home/rakesh/Desktop/sample.txt"
#sourceSize = os.stat(filepath).st_size
with open(filepath, "r+") as file:
    i = 1

    while i < 13: 
        buffer = file.readlines(209715200)
        buffer.sort()
        with open("/home/rakesh/test/input"+str(i)+".txt", "w") as inFile:
            inFile.write(''.join(buffer))
        buffer.clear()
        i += 1

sortMerge(filePath):
    from os import listdir
    from os.path import isfile, join
    inputFiles = [i for i in listdir(filePath) if isfile(join(filePath))]
    
    

