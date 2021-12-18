"""
Your task is create your own HashTable without using a built-in library.

Your HashTable needs to have the following functions:

- put(key, value) : Inserts a (key, value) pair into the HashTable. If the
value already exists in the HashTable, update the value.
- get(key): Returns the value to which the specified key is mapped, or -1 if
this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the
mapping for the key.

Example:

```plaintext
hash_table = MyHashTable();
hash_table.put("a", 1);
hash_table.put("b", 2);
hash_table.get("a");            // returns 1
hash_table.get("c");            // returns -1 (not found)
hash_table.put("b", 1);         // update the existing value
hash_table.get("b");            // returns 1
hash_table.remove("b");         // remove the mapping for 2
hash_table.get("b");            // returns -1 (not found)
```
"""
# linked-list class constructor:
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashTable:

    def __init__(self, capacity=8):
        self.storage = [None] * capacity
        self.capacity = capacity
        self.item_count = 0

    def hash(self, key):
        # DJB2 standard hashing function
        str_key = str(key).encode()

        # start with arbitrarily large prime
        hash_value = 5381

        # Bit shift
        for b in str_key:
            hash_value = ((hash_value << 5) + hash_value) + b
            hash_value &= 0xffffffff

        return hash_value % self.capacity


    def get(self, key):

        index = self.hash(key)
        return self.storage[index][1]

    def put(self, key, value):
        index = self.hash(key)
        
        # look through the linked list at storage[index] to see if this key is already in the table
        currentNode = self.storage[index]
        while currentNode:
            if currentNode.key == key: # found a key in list
                #update the value
                currentNode.value = value
                return
            currentNode = currentNode.next

        # otherwise, append a new ListNode with the key and value
        newNode = ListNode(key, value)
        newNode.next = self.storage[index]
        self.storage[index] = newNode
        

    def delete(self, key):
        index = self.hash(key)
        if self.storage[index] != None:
            self.item_count -= 1
        self.storage[index] = None


        # # Increment the item count(if there wasn't something there before)
        # if self.storage[index] == None:
        #     self.item_count += 1