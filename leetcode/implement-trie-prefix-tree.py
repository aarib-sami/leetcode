class TrieNode:
    def __init__(self, value, endOfWord):
        self.val = value
        self.endOfWord = endOfWord

class Trie:

    def __init__(self):
        self.graph = defaultdict(list)
        self.root = TrieNode(0, False)

    def insert(self, word: str) -> None:
        ptr = self.root

        for i in range(len(word)):
            found = False
            for child in self.graph[ptr]:
                if child.val == word[i]:
                    ptr = child
                    found = True
                    break
            if not found:
                newNode = TrieNode(word[i], False)
                self.graph[ptr].append(newNode)
                ptr = newNode

        ptr.endOfWord = True

    def search(self, word: str) -> bool:
        ptr = self.root

        for i in range(len(word)):
            found = False
            for child in self.graph[ptr]:
                if child.val == word[i]:
                    found = True
                    ptr = child
                    break
            if not found:
                return False
        return True if ptr.endOfWord else False

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root

        for i in range(len(prefix)):
            found = False
            for child in self.graph[ptr]:
                if child.val == prefix[i]:
                    found = True
                    ptr = child
                    break
            if not found:
                return False

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)