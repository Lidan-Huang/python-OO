import random

class WordFinder(object):
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("./words.txt")
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


class SpecialWordFinder(WordFinder):
    # def __init__(self, filepath):
    #     super().__init__(filepath)
    #     self.words = self.read_file()

    def read_file(self):
        with open(self.filepath) as lines:
            return [line.strip() for line in lines
                    if (line.strip() != "" and not line.strip().startswith("#"))]
           
