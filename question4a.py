class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val: # Push sub-node to right
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else: # Push sub-node to left
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, current, find_val):
        if current:
            if current.value == find_val:
                return True
            elif current.value < find_val:
                return self.search_helper(current.right, find_val)
            else:
                return self.search_helper(current.left, find_val)
        return False

    def makeBST(self, matrix):
        for i, subnode in enumerate(matrix[self.root.value]): # Start at root row
            if subnode !=0: # if subnode is a child, insert it.
                self.insert(i)

        for i,node in enumerate(matrix):
            for j,child in enumerate(node):
                if child != 0 and i != self.root.value:
                    self.insert(j)
                    #print("Node {} has child {}".format(i,j))

    def lca(self, head_node, n1, n2):
        # Base Case
        if head_node is None:
            return None

        # # If both n1 and n2 are smaller than root, then LCA
        # # lies in left
        if(head_node.value > n1 and head_node.value > n2):
            return self.lca(head_node.left, n1, n2)

        # If both n1 and n2 are greater than root, then LCA
        # lies in right
        if(head_node.value < n1 and head_node.value < n2):
            return self.lca(head_node.right, n1, n2)

        return head_node.value



def question4(matrix, root, n1, n2):
    head = BST(root)
    head.makeBST(matrix)
    return head.lca(head.root,n1, n2)

# Main program
def main():
    print(question4([[0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 1],
                     [0, 0, 0, 0, 0]],
                     3, 1, 4))

if __name__ == '__main__':
    main()
