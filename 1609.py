root = [5,4,2,3,3,7]

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


if root is None:
    print(True)
queue = [root]
level = 0
while queue:
    prev = float('-inf') if level % 2 == 0 else float('inf')
    for _ in range(len(queue)):
        node = queue.pop(0)
        print(node)
        if (level % 2 ==0 and (node.val % 2 == 0 or node.val <= prev)) or (level % 2 != 0 and (node.val % 2 != 0 or node.val >= prev)):
            print(False)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        prev = node.val
    level +=1
print(True)