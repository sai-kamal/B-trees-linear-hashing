from node import Node

class Btree:
    def __init__(self):
        self.root = Node()

    def insert(self, node, val):
        print('insert', val)
        '''insert value into the B tree'''
        if node.is_leaf:
            return node.insert_leaf(val)
        else:
            ret = None
            ind = None  # pointer index
            new_key = None
            new_node = None
            if val < node.keys[0]:
                ret, new_key, new_node = self.insert(node.pointers[0], val)
                ind = 0
            for i in range(len(node.keys[:-1])):
                if node.keys[i] <= val and val < node.keys[i+1]:
                    ret, new_key, new_node = self.insert(node.pointers[i+1], val)
                    ind = i+1
            if node.keys[-1] <= val:
                ret, new_key, new_node = self.insert(node.pointers[-1], val)
                ind = len(node.keys)
            
            if ret == 0:
                return 0, None, None
            elif ret == 1:
                return node.insert_non_leaf(ind, new_key, new_node)

    def change_root(self, ret, val, pointer):
        if ret == 0:
            return
            # current node if full, so split it
        # # if len(self.keys) < Node.num_keys:
        # #     self.keys.append(val)
        # #     self.keys = sorted(self.keys)
        # #     self.pointers = self.pointers[:ind+1] + [pointer] + self.pointers[ind+1:]
        # #     return 0, None, None  # 0 is the return val when val is inserted into the present node
        # else:
        node = Node()
        node.keys.append(val)
        node.pointers = [self.root]
        node.pointers.append(pointer)
        node.is_leaf = False
        self.root = node
        return
    
    def find(self, val):
        '''find value in the B tree if present else return -1'''
        print('find', val)
        self.print()

    def count(self, val):
        '''count instances of val in the B tree'''
        print('count', val)
        self.print()

    def range(self, x, y):
        '''count number of values present in the range'''
        print('range', x, y)
        self.print()

    def print(self):
        '''print the btree level wise'''
        self.root.print()
