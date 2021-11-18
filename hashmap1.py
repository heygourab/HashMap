# hashmap ->
# look up by key is O(1) on avarange
# Inserting/Deletins is O(1) on avarage
# array ->
# look up by index is O(1) on avarange
# Inserting/Deletins is O(n) on avarage


class Hashmap:
    def __init__(self, ):
        self.arr = [None] * 100  #arr = [none, none , none ,....100n]

    def get_hash(self, key):
        store = 0
        for i in key:
            store += ord(i)  #ord return a ascii value of a string
        return store % 100

    def __setitem__(self, key, value):
        key = self.get_hash(key)
        self.arr[key] = value

    def __getitem__(self, key):
        key = self.get_hash(key)
        if self.arr[key] is None:
            return 'Wrong key!'
        return self.arr[key]

    def __delitem__(self, key):
        key = self.get_hash(key)
        self.arr[key] = None


if __name__ == '__main__':
    h = Hashmap()  #object of the HashMap class

    h['gourab'] = 69  #set hash value
    h['heygourab'] = 108  #set hash value
    h['rupam'] = 143  #set hash value

    print(h['gourab'])  #get hash value
    print(h['heygourab'])  #get hash value
    print(h['rupam'])  #get hash value

    del h['heygourab']  #delete hash value
    print(h['heygourab'])  #now hash value is None
