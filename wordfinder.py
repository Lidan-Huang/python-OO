import random

class LineFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = LineFinder("./words.txt")
    5 words read
    """

    def __init__(self, filepath):
        """Create a generator to get and print words"""
        self.filepath = filepath
        self.words = self.read_file()
        print(f"{len(self.words)} words read")

    def read_file(self):
        """Read file and return a list of words"""
        with open(self.filepath) as lines:
            return [line.strip() for line in lines]
        
    def random(self):
        """Get the random word from the words list"""
        return random.choice(self.words)
