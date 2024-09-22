from collections import defaultdict as dd
class TrieNode:
    def __init__(self):
        self.children = dd(TrieNode)
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_end = True

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_end
    
    def startsWith(self, prefix: str) -> bool:
        current = self.root 
        for letter in prefix:
            current = current.children.get(letter)
            if not current:
                return False
        return True
    
trie = Trie()

trie.insert("apple")
print("Searching for 'apple':", trie.search("apple")) 
print("Searching for 'app':", trie.search("app"))     
print("Checking if 'app' is a prefix:", trie.startsWith("app")) 
print()

trie.insert("app")
print("Searching for 'app':", trie.search("app")) 
print()

trie.insert("bat")
trie.insert("bath")
trie.insert("batman")
print("Searching for 'bat':", trie.search("bat")) 
print("Searching for 'bath':", trie.search("bath")) 
print("Searching for 'batman':", trie.search("batman")) 
print()

print("Searching for 'bats' (should not exist):", trie.search("bats")) 
print("Checking if 'ba' is a prefix:", trie.startsWith("ba")) 
print("Checking if 'batm' is a prefix:", trie.startsWith("batm")) 

