class HashTable:
    def __init__(self):
        self.collection = dict()

    def hash(self, string):
        ASCII_values = 0
        for char in string:
            ASCII_values += ord(char)
        
        return ASCII_values
    
    def add(self, key, value):
        current_hash = self.hash(key)
        if current_hash not in self.collection.keys():
            self.collection[current_hash] = {}
        self.collection[current_hash][key] = value

    def remove(self, key):
        h = self.hash(key)
        if h in self.collection and key in self.collection[h]:
            del self.collection[h][key]
        else:
            pass

    def lookup(self, key):
        h = self.hash(key)
        if h in self.collection and key in self.collection[h]:
            return self.collection[h][key]
        else:
            return None        
