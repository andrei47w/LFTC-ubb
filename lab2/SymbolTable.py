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

        return hashPos, listPos

    def findByPair(self, hashPos, listPos):
        if self.__capacity <= hashPos or len(self.__items[hashPos]) <= listPos:
            return 0

        return self.__items[hashPos][listPos]



table_capacity = 25
identifiers = SymbolTable(table_capacity)
int_constants = SymbolTable(table_capacity)
str_constants = SymbolTable(table_capacity)

# print(identifiers.add("-"))
# print(identifiers.add("+"))
# print(identifiers.add("=="))
# print(identifiers.findByPair(1, 2))
#
# print(identifiers.getPos("-"))
# print(identifiers.getPos("+"))
# print(identifiers.getPos("=="))
