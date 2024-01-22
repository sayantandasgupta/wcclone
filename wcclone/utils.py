def countBytes(fileData: list) -> int:
    numBytes = 0

    for b in fileData:
        numBytes += len(b)
    return numBytes


def countLines(fileData: list) -> int:
    return len(fileData)


def countWords(fileData : list) -> int:
    numWords = 0

    for i in range(len(fileData)):
        fileData[i] = fileData[i].decode()
    
    for line in fileData:
        numWords += len(line.strip().split())

    return numWords

