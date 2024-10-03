class Trie:

    def __init__(self):
        self.storage = {}
        self.fullList = []

    def insert(self, word: str) -> None:
        if word in self.storage:
            self.storage[word] += 1
            self.fullList.append(word)
        else:
            self.storage[word] = 1
            self.fullList.append(word)

    def countWordsEqualTo(self, word: str) -> int:
        if word not in self.storage:
            return 0
        else:
            return self.storage[word]

    def countWordsStartingWith(self, prefix: str) -> int:
        counter = 0
        for word in self.fullList:
            if prefix == word[:len(prefix)]:
                counter += 1
        return counter

    def erase(self, word: str) -> None:
        # removing the element from a map and all instances in a list
        if word in self.storage and self.storage[word] > 0:
            self.storage[word] -= 1
            self.fullList.remove(word)
        return

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)

def main():
    obj = Trie()

    word = "apple"
    prefix = "app"

    obj.insert(word)
    obj.insert(word)

    param2 = obj.countWordsEqualTo(word)
    param3 = obj.countWordsStartingWith(prefix)
    obj.erase(word)

    solution = [2, 2]
    output = [param2, param3]
    if solution != output:
        print("ERROR::::\nHere is your output: {}\n Here is the solution: {}".format(output, solution))
    else:
        print("Solution is correct!")

main()
