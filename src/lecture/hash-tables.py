'''
Hash Tables: Javascript objects, python dictionaries, hashmaps
    - Made up of key/value pairs
    - get --> O(1) Time complexity
    - insert --> O(1) Time complexity
    - delete --> O(1) Time complexity
    - Space Complexity --> O(n)
    - not good for searching, no order
    - Are built by abstracting on top of an array
        - keys are run through a hashing function to convert it to an index number, then the value is placed into the corresponding index of an array of pre-determined length.
        - when the value is retrieved, the key is hashed again and the operation becomes a simple array index lookup O(1) operation
    - Hash Function: takes an input (in this case a string) and outputs a number
        - for a specific input, it must ALWAYS return the same output
'''
# Construct a class that builds a hash table dictionary instance
class Dict:

    def __init__(self, capacity=8):
        self.storage = [None] * capacity # initializes specified storage capacity of the array
        self.capacity = capacity # stores capacity as a variable
        self.item_count = 0 # keeps track of how many real items are in storage

    # Hashing Function: pass in a string (key) and the size of the array the values will be stored in
    def hash(self, string):
        # encode turns a string into its binary representation --> O(n) Time complexity
        bytes = string.encode()
        # transform out bytes representation of the string into a number
        sum = 0
        for byte in bytes: # --> O(n) Time complexity
            sum += byte
        return sum % self.capacity # by modulating the sum, the resulting integer will always be between 0 and the modulator (capacity defined upon instantiating the dictionary) ensuring a corresponding index in the array exists

    def get(self, key):
        # use class method hash to hash the key to get an index
        index = self.hash(key)
        # return the corresonding index of the hashed key, make sure to return the value which is the second item in the index's tuple
        return self.storage[index][1]

    def insert(self, key, value):
        # use class method hash to hash the key to get an index
        index = self.hash(key)
        # if no preexisting value in this index increment the count
        if self.storage[index] == None:
            self.item_count += 1
        # use the hashed index derived from the key to set the index of our storage to a tuple containing the key name and the corresponding value
        self.storage[index] = (key, value)
        

    def delete(self, key):
        # use class method hash to hash the key to get an index
        index = self.hash(key)
        # if there is an item at the hashed index, decrement count
        if self.storage[index] != None:
            self.item_count -= 1
        # set the index derived from the hashed key back to None
        self.storage[index] = None

    # these dunder methods allow some default behavior expected of a python dictionary, i.e. square bracket notation to access the dict, curly brackets to instantiate one, and len to get count of items
    def __setitem__(self, key, value):
        return self.insert(key, value)
    def __getitem__(self, key):
        return self.get(key)
    def __len__(self):
        return self.item_count


food = Dict()
food.insert('apple', 'fruit')
food.insert('cucumber', 'vegetable')
food.insert('cheese', 'fungus')
apple = food.get('apple')
food.delete('cucumber')

print(apple)
print(len(food))
