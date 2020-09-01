class hashing:
    def __init__(self, n):
        self.hashtable = [None]*n

    def hashfucn(self, num):
        return num % 6

    def insert(self, num, hashtable):
        hashvalue = self.hashfucn(num)
        if self.hashtable[hashvalue] != None:
            self.hashtable[hashvalue].append(num)
        else:
            self.hashtable[hashvalue] = [num]

    def search(self, num):
        hashval = self.hashfucn(num)
        if num in self.hashtable[hashval]:
            return True
        else:
            return False


if __name__ == "__main__":
    ob = hashing(6)
    elements = [i for i in range(100)]
    for element in elements:
        ob.insert(element, ob.hashtable)
    print(ob.hashtable)
    print(ob.search(24))
