class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, item):
        if not isinstance(item, str):
            return item
        result = 0
        for i in item: 
            result +=  ord(i)
        return result
        
    def add(self, key, value):
        hashed = self.hash(key)

        if hashed in self.collection:
        # ADD to existing dictionary
            self.collection[hashed][key] = value
        else:
        # CREATE a new dictionary
            self.collection[hashed] = {key: value}

        return self.collection

    
    def remove(self, key):
        
        hashed = self.hash(key)
        if hashed in self.collection:
            
            self.collection.pop(key, None)
            self.collection
            
    def lookup(self, key):
        if key in self.collection:
            return self.collection[key]
example = HashTable()
print(example.add(1, "a"))
print(example.add(2, "b"))
print(example.add(2, "f"))

# print(example.remove(3))
