
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

        if self.length == 0:
            self.add_front(value)
            return

        # get to the back
        runner = self.head
        while runner.next != None:
            runner = runner.next
        
        runner.next = newNode
        # add new node to back.next


    def concat(self, sll2):

        # self: [1,2,3], ssl2: [5,6,7]  => [1,2,3,5,6,7]

        # todo: travel to end of self list
        
        runner = self.head
        while runner.next != None:
            runner = runner.next

        # attach last node to head of ssl2
        runner.next = sll2.head


    def zip(self, misty):

        # self: [1,2,3], sll2 [4,5,6] => [1,4,2,5,3,6]

        runner = self.head
        t1 = runner.next

        runner.next = misty.head

        runner = runner.next
        t2 = runner.next

        while runner.next != None:
            
            runner.next = t1
            runner = runner.next
            t1 = runner.next
                
            runner.next = t2
            runner = runner.next
            t2 = runner.next
            
            if t1 != None:
                break



        

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

    @property
    def length(self):
        # returns number of nodes in list

        runner = self.head
        count = 0
        # move through list, counting each time
        while runner != None:
            count += 1
            runner = runner.next

        
        return count

    def max(self):
        # returns largest value in list
        runner = self.head
        currMax = runner.value
        # move through list, comparing to currMax
        while runner != None:
            if currMax < runner.value:
                currMax = runner.value
            runner = runner.next

        return currMax

    def is_palindrome(self):

        # [2,4,6,4,2] => True
        # [1,2,3,4] => False

        # convert sll to py list
        newList = []

        runner = self.head
        # iterate list, append each node's value to list
        while runner != None:
            newList.append(runner.value)
            runner = runner.next

        # then compare (last - i) to (first + i)
        for i in range(int(len(newList) / 2)):
            if newList[i] != newList[(len(newList) - 1) - i]:
                return False

        return True
    
    def remove_value(self, val):
        
        # EDGE CASE (FIRST ONE)
        if self.head.value == val:
            to_return = self.head.value
            self.head = self.head.next
            return to_return
            # do stuff

        runner = self.head.next
        # maintaing a "prev" pointer
        prev = self.head
        # loop through list
        while runner.next != None:
            if runner.value == val:
                # save it
                to_return = runner.value
                # kill it
                prev.next = runner.next
                # return it
                return to_return

            prev = runner
            runner = runner.next

        # EDGE CASE (LAST ONE)
        if runner.value == val:
            to_return = runner.value
            prev.next = None
            return to_return


    def remove_negatives(self):
        
        # EDGE CASE (FIRST ONE)
        while self.head.value < 0:
            self.head = self.head.next

        # remove all negative values (< 0)

        runner = self.head
        # loop through list 
        while runner.next != None:
            
            # stay one behind

            # EDGE CASE (CONSECTUTIVE NEGATIVES)
            while runner.next.value < 0:
                # check if runner.next is None
                if runner.next.next == None:
                    runner.next = None
                    return

                # kill it
                runner.next = runner.next.next


            runner = runner.next
                




    def __repr__(self):
        output = "["

        if self.head == None:
            return output + "]"

        runner = self.head
        

        while runner.next != None:
            output += f"{runner.value}, "
            runner = runner.next

        output += f"{runner.value}"
        # loop list, concat values
        output += "]"
        return output
