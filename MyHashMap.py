class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.data[key] = value
        
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.data and  key in self.data.keys():
            return self.data[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if self.data and  key in self.data.keys():
            return self.data.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
myHashMap = MyHashMap()
myHashMap.put(1, 1) # The map is now [[1,1]]
myHashMap.put(2, 2) # The map is now [[1,1], [2,2]]
print(myHashMap.get(1))  # return 1, The map is now [[1,1], [2,2]]
print(myHashMap.get(3))    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1) # The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(myHashMap.get(2))    # return 1, The map is now [[1,1], [2,1]]
print(myHashMap.remove(2)) # remove the mapping for 2, The map is now [[1,1]]
print(myHashMap.get(2))    # return -1 (i.e., not found), The map is now [[1,1]]
