def countBytes(file: str) -> int:
    try:
        with open(file, 'rb') as f:
            byteArray = f.readlines()
            numBytes = 0

            for b in byteArray:
                numBytes += len(b)
            return numBytes
    except FileNotFoundError:
        raise FileNotFoundError


def countLines(file: str) -> int:
    try:
        with open(file) as f:
            lines = f.readlines()
            numLines = len(lines)

            return numLines
    except FileNotFoundError:
        raise FileNotFoundError


def countWords(file: str) -> int:
    try:
        with open(file) as f:
            lines = f.readlines()
            numWords = 0

            for line in lines:
                words = line.strip().split()
                numWords += len(words)

        return numWords
    except FileNotFoundError:
        raise FileNotFoundError
