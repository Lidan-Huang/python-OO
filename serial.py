
class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Make a new generator, starting at the start."""
        self.start = start
        self.next = start

    def generate(self):
        """Generate the next serial number."""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset the number to start"""
        self.next = self.start