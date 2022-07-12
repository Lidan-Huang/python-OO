class LineFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = LineFinder("./words.txt")
    5 words read
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.words = self.read_file()
        print(f"{len(self.words)} words read")

    def read_file(self):
        with open(self.filepath) as lines:
            return [line.strip() for line in lines]
        
