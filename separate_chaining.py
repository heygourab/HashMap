# 1.separate chaining (open hashing):
# > This technique creates a linked list to the slot for which collision occurs.
# > > The new key is then inserted in the linked list.
# > > > These linked lists to the slots appear like chains.
# > > > > That is why, this technique is called as separate chaining.

# for searching time complexity is O(1) on worst case time complexity O(n).
# for deletion time complexity in O(n).


class HashTable:
    def __init__(self, ):
        self.array = [[] for i in range(10)]

    def hash(self, key):
        store = 0
        for i in key:
            store += ord(i)
        return store % 10

    def __setitem__(self, key, value):
        h = self.hash(key)
        found = False
        # update the value thats exists
        for idx, element in enumerate(self.array[h]):
            if len(element) == 2 and element[0] == key:
                self.array[h][idx] = [key, value]
                found = True
                break
        if found == False:
            # add new value to the hash array
            self.array[h].append([key, value])

    def __getitem__(self, key):
        h = self.hash(key)
        for element in self.array[h]:
            if element[0] == key:
                return element[1]
        return 'Wrong Key!'

    def __delitem__(self, key):
        h = self.hash(key)
        for idx, element in enumerate(self.array[h]):
            if len(element) == 2 and element[0] == key:
                del self.array[h][idx]


if __name__ == '__main__':
    hm = HashTable()
    hm['gourab'] = 69
    hm['return'] = 108
    hm['hash'] = 10
    hm['print'] = 19
    hm['prokash'] = 70
    print(hm['gourab'])
    print(hm.array)