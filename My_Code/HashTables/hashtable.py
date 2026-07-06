class HashTable:
    def __init__(self,size = 7):
        self.data_map = [None] * size
    
    def hash(self,key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) *23) % len(self.data_map)
        return my_hash
    
    def set_item(self,key,value):
        index = self.hash(key)
        if self.data_map[index] == None:    
            self.data_map[index] = []
        self.data_map[index].append([key,value])
    
    def get_item(self,key):
        index = self.hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
    
    def get_key(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys
    
    def printHashTable(self):
        for i , val in enumerate(self.data_map):
            print(i,":",val)

my_hash_table = HashTable()
my_hash_table.set_item('washers',50)
my_hash_table.set_item('bolts',1400)

print(my_hash_table.get_item('washers'))
print(my_hash_table.get_item('bolts'))
print(my_hash_table.get_item('nuts'))

my_hash_table.printHashTable()
            
        
            