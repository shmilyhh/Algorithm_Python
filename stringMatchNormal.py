class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        if len(word) == 0:
            return
        i = 0
        current = self.root
        while i < len(word):
            if current.children[ord(word[i])-ord('a')] is None:
                node = TrieNode()
                current.children[ord(word[i])-ord('a')] = node
            current = current.children[ord(word[i])-ord('a')]
            i += 1
        current.isWord = True
    
    def searchRe(self, word, current, i):
        if i == len(word):
            if current.isWord:
                return True
            return False
        
        result = False
        
        if word[i] == ".":
            for child in current.children:
                if child != None:
                    if self.searchRe(word, child, i+1):
                        result = True 
        else:
            if current.children[ord(word[i])-ord('a')] != None:
                if self.searchRe(word, current.children[ord(word[i])-ord('a')], i+1):
                    result = True
        return result
        
    def search(self, word):
        if len(word) == 0:
            return False
        
        return self.searchRe(word, self.root, 0)

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