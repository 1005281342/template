from collections import deque


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        self.is_word = "*#is_word#*"

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for c in word:
            if c not in node.keys():
                node[c] = dict()
            node = node[c]
        node[self.is_word] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        dq = deque()
        dq.append((node, 0))
        while dq:
            node, i = dq.popleft()
            if node is True:
                continue
            if i == len(word):
                if self.is_word in node.keys():
                    return True
                else:
                    continue
            if word[i] in node.keys():
                dq.append((node[word[i]], i + 1))
            elif word[i] == '.':
                for k in node.keys():
                    dq.append((node[k], i + 1))
        return False
