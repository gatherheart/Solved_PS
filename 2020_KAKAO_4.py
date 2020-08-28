from collections import defaultdict

QUESTION_MARK = "?"

class TrieNode:

    def __init__(self):
        super().__init__()
        self.childrens = [None] * 26
        self.letter = ""
        # classified by key length
        self.counts = defaultdict(int)


class Trie:

    def __init__(self):
        super().__init__()
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):

        pointer = self.root
        len_of_key = len(key)
        
        for i in range(len_of_key):
            index = self._char_to_index(key[i])

            if not pointer.childrens[index]:
                pointer.childrens[index] = self.getNode()    
                pointer.childrens[index].letter = key[i]

            pointer.counts[len_of_key] += 1            
            pointer = pointer.childrens[index]

    def search(self, key):

        pointer = self.root
        len_of_key = len(key)

        for i in range(len_of_key):
            index = self._char_to_index(key[i])

            if key[i] == QUESTION_MARK:
                return True, pointer.counts[len_of_key]

            elif not pointer.counts[len_of_key]:
                return False, 0
            elif not pointer.childrens[index]:
                return False, 0

            pointer = pointer.childrens[index]

        return True, pointer.counts[len_of_key]

    def traverse(self, key):
        pointer = self.root
        len_of_key = len(key)
        ret = ""

        for i in range(len_of_key):
            index = self._char_to_index(key[i])

            if not pointer.childrens[index]:
                return ret, pointer.count

            pointer = pointer.childrens[index]
            ret += pointer.letter 
            
        return ret, pointer.counts[len_of_key]
        

def solution(words, queries):
    answer = []
    cache = defaultdict(int)
    word_tree = Trie()
    inv_word_tree = Trie()

    for word in words:
        word_tree.insert(word)
        inv_word_tree.insert(word[::-1])

    for query in queries:

        if cache[query]:
            answer.append(cache[query])
            continue

        if query[0] != QUESTION_MARK:
            result = word_tree.search(query)
            answer.append(result[1])
            cache[query] = result
        else:
            result = inv_word_tree.search(query[::-1])            
            answer.append(result[1])
            cache[query] = result

        

    return answer


if __name__ == "__main__":
    words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
    queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

    print(solution(words, queries))
    

