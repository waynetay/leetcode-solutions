class Node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None
firstNode = Node(1)
secondNode = Node(7)
thirdNode = Node(9)
fourthNode = Node(2)
fifthNode = Node(6)
sixthNode = Node(5)
seventhNode = Node(11)
eigthNode = Node(9)
ninthNode = Node(5)

firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode
secondNode.right = fifthNode
fifthNode.left = sixthNode
fifthNode.right = seventhNode
thirdNode.right = eigthNode
eigthNode.left = ninthNode


print(firstNode.right.right.left.data)


