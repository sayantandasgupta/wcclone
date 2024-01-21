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

def countLines(file : str) -> int:
    try:
        with open(file) as f:
            lines = f.readlines()
            numLines = len(lines)
            
            return numLines
    except FileNotFoundError:
        raise FileNotFoundError
    
def countWords(file : str) -> int:
    pass