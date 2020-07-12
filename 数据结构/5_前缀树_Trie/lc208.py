class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # 初始化根节点
        self.root = dict()

        # 单词标识
        self.is_word = "*#is_word#*"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # 当前节点为根节点
        node = self.root
        for s in word:
            # 如果该字符不在node中则进行创建
            if s not in node.keys():
                node[s] = dict()
            # 移动当前节点
            node = node[s]
        # 标记这是一个单词
        node[self.is_word] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        # 当前节点为根节点
        node = self.root
        for s in word:
            # 该字符不在节点中则说明该单词不在单词列表中
            if s not in node.keys():
                return False
            node = node[s]

        return self.is_word in node.keys()

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # 当前节点为根节点
        node = self.root
        for s in prefix:
            # 该字符不在节点中则说明该单词不在单词列表中
            if s not in node.keys():
                return False
            node = node[s]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
