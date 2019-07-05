
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

    def size(self):

        runner = self.head
        count = 0

        if self.head == None:
            return count

        while runner.next != None:
            count += 1
            runner = runner.next

        count += 1

        return count

    def remove_front(self):

        if self.size() == 0:
            raise Exception("No nodes to remove!")

        to_return = self.head.value
        self.head = self.head.next
        return to_return

    def remove_back(self):

        # Edge Case: 2 nodes or less need special care
        
        nodes = self.size()
        runner = self.head

        if nodes == 0:
            raise Exception("No nodes to remove!")

        to_return = self.head.value

        if nodes == 2:
            to_return = runner.next.value
            runner.next = None
        elif nodes == 1:
            self.head = None

        else:
        # 1 Move to 2nd to last node

            while runner.next.next != None:
                runner = runner.next
            
            
            # 2 set next to None
            to_return = runner.next.value

            # in C this would be delete runner.next
            runner.next = None
        return to_return

    def __repr__(self):
        output = "["

        runner = self.head

        while runner.next != None:
            output += f"{runner.value}, "
            runner = runner.next

        output += f"{runner.value}"
        # loop list, concat values
        output += "]"
        return output
        



        

listy = SinglyLinkedList()
listy.add_front("Sally")
listy.add_back("Marcia")
listy.add_back("Donny")
listy.add_back("Suzie")
print(listy)


