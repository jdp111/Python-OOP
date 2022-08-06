"""Word Finder: finds random words from a dictionary."""


from random import randint

class WordFinder:
    """reads a text file and allows user to select a random word"""
    def __init__(self,file):
        """makes a wordlist of words with end line on the end"""
        myFile = open(file,"rt").readlines()
        self.wordList = [word.rstrip('\n') for word in myFile]
        
    def __repr__(self): 
        """shows the user info about the word list"""
        return (f"{len(self.wordList)} words read")
    
    def random(self):
        index = randint(0,len(self.wordList)-1)
        return self.wordList[index]

class SpecialWordFinder(WordFinder):
    """all functions of WordFinder, but allows blank lines in the text file"""
    def __init__(self,file):
        super().__init__(file)
        self.wordList = [word for word in self.wordList if word and not word[0] == '#']