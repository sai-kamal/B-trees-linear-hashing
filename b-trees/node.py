import math

class Node:
    num_keys = 3
    def __init__(self):
        self.is_leaf = True
        self.keys = []
        self.pointers = []
        self.next = None

    def insert_leaf(self, val):
        '''insert val into the leaf'''
        if len(self.keys) < Node.num_keys:
            self.keys.append(val)
            self.keys = sorted(self.keys)
            return 0, None, None  # 0 is the return val when val is inserted into the present node
        else:
            # current node if full, so split it
            new_node = self.split_leaf(val)
            return 1, new_node.keys[0], new_node

    def split_leaf(self, val):
        '''split the current leaf node when it is full'''
        self.keys.append(val)
        self.keys = sorted(self.keys)
        new_node = Node()
        divider = math.ceil( (Node.num_keys+1)/2 )
        new_node.keys = self.keys[divider:]
        self.keys = self.keys[:divider]
        self.next = new_node
        return new_node

    def insert_non_leaf(self, ind, val, pointer):
        '''insert val into the non leaf'''
        if len(self.keys) < Node.num_keys:
            self.keys.append(val)
            self.keys = sorted(self.keys)
            self.pointers = self.pointers[:ind+1] + [pointer] + self.pointers[ind+1:]
            return 0, None, None  # 0 is the return val when val is inserted into the present node
        else:
            # current node if full, so split it
            new_key, new_node = self.split_non_leaf(ind, val, pointer)
            return 1, new_key, new_node

    def split_non_leaf(self, ind, val, pointer):
        '''split the current non leaf node when it is full'''
        new_node = Node()
        new_node.is_leaf = False
        self.keys.append(val)
        self.keys = sorted(self.keys)
        divider = math.ceil((Node.num_keys+1)/2)
        new_node.keys = self.keys[divider+1:]
        new_key = self.keys[divider]
        self.keys = self.keys[:divider]
        self.next = new_node
        self.pointers = self.pointers[:ind+1] + [pointer] + self.pointers[ind+1:]
        new_node.pointers = self.pointers[divider+1:]
        self.pointers = self.pointers[:divider+1]
        return new_key, new_node

    def operate(self, val, val2):
        '''find if val is present in the current node
        or its next neigbhours'''
        count = 0
        for key in self.keys:
            if key >= val and key <= val2:
                count += 1
            elif key > val2:
                return count
        if self.next is not None:
            return count + self.next.operate(val, val2)
        return count
        
    def print(self):
        for key in self.keys[:-1]:
            print(key, end=', ')
        print(self.keys[-1], end='\t')
