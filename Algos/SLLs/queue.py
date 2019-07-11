from node import Node, SinglyLinkedList

class Queue(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    def is_empty(self):
        return self.head == None and self.tail == None

    def dequeue(self):

        if self.head == None:
            raise Exception("EMPTY QUEUE LOL")
        
        x = self.head.value
        self.head = self.head.next
        # EDGE CASE: reducing to empty queue
        if self.head == None:
            self.tail = None
        return x

    def enqueue(self, value):

        newNode = Node(value)

        # EDGE CASE: empty queue
        if self.is_empty():
            self.head = newNode
            self.tail = newNode  

        # otherwise we can just extend tail
        self.tail.next = newNode
        self.tail = newNode

    def add_back(self, value):
        self.enqueue(value)
        
    def remove_back(self):
        pass

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)

print(queue.dequeue())
print(queue)
