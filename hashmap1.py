# hashmap ->
# look up by key is O(1) on avarange
# Inserting/Deletins is O(1) on avarage
# array ->
# look up by index is O(1) on avarange
# Inserting/Deletins is O(n) on avarage


class Hashmap:
    def __init__(self, ):
        self.arr = [None
                    for i in range(101)]  #arr = [none, none , none ,....100n]

    def get_hash(self, key):
        store = 0
        for i in key:
            store += ord(i)  #ord return a ascii value of a string
        return store % 100

    def __setitem__(self, key, value):
        self.arr[self.get_hash(key)] = value

    def __getitem__(self, key):
        if self.arr[self.get_hash(key)] is None:
            raise KeyError(key)
        return self.arr[self.get_hash(key)]

    def __delitem__(self, key):
        self.arr[self.get_hash(key)] = None


if __name__ == '__main__':
    pass
