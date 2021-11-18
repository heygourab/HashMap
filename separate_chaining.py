# 1.separate chaining (open hashing):
# > This technique creates a linked list to the slot for which collision occurs.
# > > The new key is then inserted in the linked list.
# > > > These linked lists to the slots appear like chains.
# > > > > That is why, this technique is called as separate chaining.

# for searching time complexity is O(1) on worst case time complexity O(n).
# for deletion time complexity in O(n).


class HashTable:
    def __init__(self):
        self.array = [[]] * 100

    def get_hash(self, key):
        store = 0  # store
        for k in key:
            store += ord(k)

    def __setitem__(self, key, value):
        key = self.get_hash(key)
        
        
        for idx, v in enumerate(self.array):
            if len(v) == 2 and v[0] == key
        self.array[key].append(key,value)
        
        
        
        

    def __delitem__(self, key):
        key = self.get_hash(key)
        self.array[key] = None

    def __getitem__(self, key):
        key = self.get_hash(key)
        return self.array[key]


if __name__ == '__main__':
    h = HashTable()
    h['gourab'] = 69
    print(h.array)
