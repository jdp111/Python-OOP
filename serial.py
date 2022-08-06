"""Python serial number generator."""

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
        """allows user to set the starting number"""
        self.start = start
        self.number = start
    
    def generate(self):
        """causes the counter to tick and increase by one"""
        self.number +=1
        return self.number-1
    
    def reset(self):
        """resets counter back to user specified start"""
        self.number = self.start
        