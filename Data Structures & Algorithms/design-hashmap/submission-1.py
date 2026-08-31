class MyHashMap:

    def __init__(self):
        self.my_list = []

    def put(self, key: int, value: int) -> None:
        # check if the key is in the list
        for n in self.my_list:
            k = n[0]

            if key == k:
                n[1] = value
                return
        
        self.my_list.append([key, value])

    def get(self, key: int) -> int:
        for n in self.my_list:
            k = n[0]
            if key == k:
                return n[1]
        
        return -1

    def remove(self, key: int) -> None:
        for i in range(0, len(self.my_list)):
            
            k = self.my_list[i][0]

            if key == k:
                self.my_list.pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)