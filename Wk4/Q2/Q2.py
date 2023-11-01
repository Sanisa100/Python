#Q2
# Implementation of Stack
class Node:
    # {
    """
    Representing a node consisting of
    - datum: the datum stored at the node
    - next: reference to the next node
    """

    def __init__(self, datum, next):
        # {
        self.datum = datum
        self.next = next
    # }


# }

class MyDigitQueue:
    # {
    """
    Implementation of a LIFO Stack as a linked list
    that connect topNode -> node -> node -> ... -> NULL
    """

    def __init__(self):
        # {
        """
        Constructs an empty stack
        """
        self.topNode = None

    # }

    def front(self):
        # {
        """
        Returns the item stored at the top of the stack,
        but do not remove it.
        If the stack is empty then returns None.
        """
        if self.topNode == None:
            return None

        return self.topNode.datum

    # }

    def enqueue(self, item):
        # {
        """
        Adds an item to the top of the stack
        """

        # create a new node to be put at the top of the stack
        newNode = Node(datum=item, next=None)

        if self.topNode == None:
            # stack is empty
            self.topNode = newNode
        else:
            newNode.next = self.topNode
            self.topNode = newNode

    # }

    def dequeue(self):
        # {
        """
        Removes the item stored at the top of the stack and returns it.
        If the stack is empty then returns None.
        """

        # if the stack is empty
        if (self.topNode == None):
            return None

        # get the item stored at the top node
        item = self.topNode.datum

        # reset the top node of this stack
        self.topNode = self.topNode.next

        return item
    # }


# }


# testing my stack
# creating a stack
queueObj = MyDigitQueue()

# push() add item to the stack
queueObj.enqueue(23)
queueObj.enqueue(7)
queueObj.enqueue(-10)

# top() get top item of the stack, but do not remove it
print(queueObj.front())
print(queueObj.front())

# pop() remove item from stack in LIFO order
print(queueObj.dequeue())
print(queueObj.dequeue())

