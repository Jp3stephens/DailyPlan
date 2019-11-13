
class vectorClass(object): 
    
    def __init__(self): 
        self.arr = [None] * 1
        self.capacity = 1 #start with capacity of 1
        self.current = 0
    
    def push(self, data): 
        #check if there is room for element
        if self.current < self.capacity: 
            self.arr[self.current] = data; 
            self.current += 1
        else: #there is no room
            #resize 
            temp = [None] * (self.capacity*2)
            for i in range(0, self.capacity): 
                temp[i] = self.arr[i]
            del self.arr 
            self.capacity *= 2
            self.arr = temp
            self.arr[self.current] = data
            self.current += 1
    

    def pushIt(self, data, index): 
        #if curr >= capacity then its problem above
        if index == self.capacity: 
            self.push(data)
        else: 
            self.arr[index] = data
    def get(self, index): 
        if index < self.current: 
            return self.arr[index]
    def pop(self): 
        self.current -= 1
    def size(self): 
        return self.current
    def getCapacity(self): 
        return self.capacity

    def printIt(self): 
        for i in range(0, self.current): 
            print(self.arr[i])
            
        


v = vectorClass()
v.push(10)
v.push(20)
v.push(30)
v.push(40)
v.push(50)

print("Vector Size: ")
print(v.size())
print("\n") 
print("Vector capacity: ")
print(v.getCapacity())
print("\n")
print("Vector elements: ")
print(v.printIt())
v.pushIt(100, 1)
print("After updating 1st index")
print("Vector elements")
print(v.printIt())
print("Element at 1st index")
print(v.get(1))
v.pop()
print("After deleting last element")
print("Vector size")
print(v.size())
print("Vector capacity")
print(v.getCapacity())
print("vector elements: ")
print(v.printIt())


