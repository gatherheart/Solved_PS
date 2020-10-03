
class TrieNode:
    def __init__(self):
        super().__init__()
        self.childrens = [None] * 26
        self.count = 0
        self.letter = ""
        self.isLeaf = False

class Trie:

    def __init__(self):
        super().__init__()
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        
        pointer = self.root
        pointer.count += 1
        len_of_key = len(key)        

        for i in range(len_of_key):
            index = self._char_to_index(key[i])
            if not pointer.childrens[index]:
                print("Insert", key, key[i])

                pointer.childrens[index] = self.get_node()
                pointer.childrens[index].letter = key[i]
            
            pointer.count += 1    
            pointer = pointer.childrens[index]

        pointer.isLeaf = True    
        
    def search(self, key):

        pointer = self.root
        len_of_key = len(key)
        
        for i in range(len_of_key):
            index = self._char_to_index(key[i])
            if pointer.childrens[index]:
                pointer = pointer.childrens[index]
            else:
                return False, 0 
        
        return True, pointer.count

    def traverse(self, key):

        pointer = self.root
        len_of_key = len(key)
        ret = ""
        
        for i in range(len_of_key):
            index = self._char_to_index(key[i])
                
            if pointer.childrens[index]:
                pointer = pointer.childrens[index]
                ret += pointer.letter
            else:
                return ret
        
        return ret

word_tree = Trie()

keys = ["the","a","there","anaswe","any", 
        "by","their"] 

for key in keys:
    word_tree.insert(key)


print(word_tree.traverse("the"))
print(word_tree.search("the"))
print(word_tree.search("th"))