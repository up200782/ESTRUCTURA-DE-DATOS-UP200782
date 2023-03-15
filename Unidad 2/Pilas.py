class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
         return self.data

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        return True if self.size == 0 else False

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def pop(self):
        dato = None
        if not self.isEmpty():
            dato = self.head.data
            self.head = self.head.next
            self.size -= 1
        return dato 

    def peek(self):
        dato = None
        if not self.isEmpty():
            dato = self.head.data
        return dato
    
    def print(self):
        cadena = ""
        temp = self.head
        while temp:
            cadena += str(temp.getData()) + " -> "
            temp = temp.next
        cadena += "None"
        print(cadena)
    
    def exists(self, element):
        temp = self.head
        while temp:
            if temp.getData() == element:
                return True
            temp = temp.next
        return False
p1 = Stack()
p1.push("Jesus")
p1.push("Maria")
p1.push("Jose")
print(p1.exists("Maria")) # True
print(p1.exists("Pedro")) # False
#p1 = Stack()
#p1.push ("Jesus")
#p1.push("Maria")
#p1.push("Jose")
#p1.print()
#print(p1.pop())
#print(p1.pop())
#print(p1.pop())
#print(p1.pop())
#print (p1.peek())