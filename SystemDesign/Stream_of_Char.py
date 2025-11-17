class TrieNode:
    def __init__(self):
        self.isLeaf = False
        self.childrens = [None] * 27

    def insert(self,word):
        node = self
        for letter in reversed(word):
            k = ord(letter) - ord('a')
            
            if node.childrens[k] is None:
                node.childrens[k] = TrieNode()
            node = node.childrens[k]
        node.isLeaf = True
    
    def search(self,word):
        node = self
        for letter in word:
            k = ord(letter) - ord('a')
            if node.childrens[k] is None:
                return False
            node = node.childrens[k]
            if node.isLeaf :
                return True
        return False
            

class StreamChecker:
    
    def __init__(self, words: List[str]):
        self.words = words
        self.trieRoot = TrieNode()
        for word in words:
            self.trieRoot.insert(word)

        self.stream =""


    def query(self, letter: str) -> bool:
        self.stream= letter + self.stream
        return self.trieRoot.search(self.stream)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
