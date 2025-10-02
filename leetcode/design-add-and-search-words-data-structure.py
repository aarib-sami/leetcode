class TrieNode():
    def __init__(self, letter, isEnd):
        self.val = letter
        self.children = {}
        self.isEnd = isEnd

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(0, False)

    def addWord(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                node = TrieNode(c, False)
                ptr.children[c] = node
            else:
                node = ptr.children[c]
            ptr = node
        node.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(c, ptr):
            if c >= len(word): return ptr.isEnd
            elif word[c] == ".":
                for child in ptr.children.values():
                    if dfs(c+1, child):
                        return True
                return False
            elif word[c] not in ptr.children:
                return False
            return dfs(c + 1, ptr.children[word[c]])
        
        return dfs(0, self.root)