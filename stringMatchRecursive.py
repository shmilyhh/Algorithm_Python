# recursive version
# match string that contains the wildcast

class Trie:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def insert(self, word):
        if word == '':
            self.isWord = True
            return
        if word[0] not in self.children.keys():
            self.children[word[0]] = Trie()
        self.children[word[0]].insert(word[1:])
        
    def search(self, word):
        if word == '':
            return self.isWord
        if word[0] == '.':
            if len(self.children.values()) == 0:
                return False
            for next in self.children.keys():
                if self.children[next].search(word[1:]):
                    return True
            return False
        else:
            if word[0] not in self.children.keys():
                return False
            return self.children[word[0]].search(word[1:])
            
class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        # Write your code here
        self.trie = Trie()


    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        # Write your code here
        self.trie.insert(word)


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        # Write your code here
        return self.trie.search(word)


# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")