
class TrieNode:
    
    def __init__(self):
        super().__init__()
        self.childrens = [None] * 26
        self.count = 0
        self.letter = ""
    
class Trie:
    
    def __init__(self):
        super().__init__()
        self.root = self.getNode()
        
    def char_to_index(self, ch):
        return ord(ch) - ord('a')
        
    def getNode(self):
        return TrieNode()    

    def insert(self, key):
        pointer = self.root
        
        for letter in key:
            index = self.char_to_index(letter)
            if not pointer.childrens[index]:
                pointer.childrens[index] = self.getNode()
                pointer.childrens[index].letter = letter        
            else:
                pointer.childrens[index].count += 1            
            pointer = pointer.childrens[index]
            
        return

    def search(self, key):
        
        pointer = self.root
        
        for letter in key:
            index = self.char_to_index(letter)
            if not pointer.childrens[index]:
                return False, 0
        
            pointer = pointer.childrens[index]
        
        return True, pointer.count
    
    def traverse(self, key):
        
        pointer = self.root
        
        for i, letter in enumerate(key):
            index = self.char_to_index(letter)
            if not pointer.childrens[index]:
                return False, 0xFFFF
        
            pointer = pointer.childrens[index]
            if pointer.count == 0:
                return True, i + 1
            
        return True, len(key)
    
def solution(words):
    answer = 0
    
    word_tree = Trie()
    for word in words:
        word_tree.insert(word)
    
   
    for word in words:
        answer += word_tree.traverse(word)[1]
    
    return answer


if __name__ == "__main__":

    test = 2
    
    if test == 1:
        words = ["go", "gone", "guild"]
    
    if test == 2:
        words = ["abc", "def", "ghi", "jklm"]

    if test == 3:
        words = ["word", "war", "warrior", "world"]
    print(solution(words))
