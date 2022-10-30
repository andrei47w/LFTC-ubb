class SymbolTable:

    def __init__(self, capacity):
        self.__items = [[]] * capacity
        self.__capacity = capacity

    def __getHash(self, key):
        hash = 0
        for char in key:
            hash += ord(char) - ord('0')
        hash %= self.__capacity

        return hash

    def add(self, key):
        if self.__contains(key):
            return self.getPos(key)
        self.__items[self.__getHash(key)].append(key)

        return self.getPos(key)

    def __contains(self, key):
        return key in self.__items[self.__getHash(key)]

    def remove(self, key):
        self.__items[self.__getHash(key)].remove(key)

    def getPos(self, key):
        hashPos, listPos = self.__getHash(key), 0
        for item in self.__items[hashPos]:
            if item != key:
                listPos += 1
            else:
                break

        return hashPos * self.__capacity + listPos

operators = SymbolTable(10)

print(operators.add("-"))
print(operators.add("+"))
print(operators.add("=="))

print(operators.getPos("-"))
print(operators.getPos("+"))
print(operators.getPos("=="))


print()
separators = SymbolTable(10)

print(separators.add(";"))
print(separators.add("\n"))
print(separators.add("{"))

print(separators.getPos(";"))
print(separators.getPos("\n"))
print(separators.getPos("{"))
