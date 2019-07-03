
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
    # name
    # best friend

class SinglyLinkedList:

    def __init__(self):
        self.head = None
    
    def add_front(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        

    def add_back(self, value):
        # make new node
        newNode = Node(value)

        # get to the back
        runner = self.head
        while runner.next != None:
            runner = runner.next
        
        runner.next = newNode
        # add new node to back.next

    def insert(self, value, position):

        if position < 2:
            self.add_front(value)
            return

        # make new node
        newNode = Node(value)

        # set up runner
        runner = self.head


        while position > 2:
            if runner.next == None:
                raise Exception("WHooopsies")
                break

            runner = runner.next
            position = position - 1

        newNode.next = runner.next
        runner.next = newNode
        



        

listy = SinglyLinkedList()
listy.add_front("Sally")
listy.add_back("Marcia")
listy.add_back("Thomas")
listy.insert("Suzie", 2)
print("LOL")

