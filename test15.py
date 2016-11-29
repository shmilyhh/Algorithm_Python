class HashTable():
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hashValue = self.hashFunction(key, len(self.slots))

        if self.slots[hashValue] == None:
            self.slots[hashValue] = key
            self.data[hashValue] = value
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = value
            else:
                nextSlot = self.rehash(hashValue, len(self.slots))
                while self.slots[nextSlot] != None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))
                
                if self.slots[nextSlot] == None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = value
                else:
                    self.data[nextSlot] = value
    
    def get(self, key):
        startSlot = self.hashFunction(key, len(self.slots))
        
        data = None
        found = False
        stop = False
        position = startSlot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startSlot:
                    stop = True
        return data

    def hashFunction(self, key, size):
        return key % size

    def rehash(self, oldHashvalue, size):
        return (oldHashvalue+1) % size

    def __setitem__(self, key, value):
        return self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)



H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)

print(H[20])

print(H[17])
H[20]='duck'
print(H[20])
print(H[99])

