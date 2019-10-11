from node import Node

class Btree:
    def __init__(self):
        self.root = Node()

    def insert(self, node, val):
        # print('insert', val)
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
        node = Node()
        node.keys.append(val)
        node.pointers = [self.root]
        node.pointers.append(pointer)
        node.is_leaf = False
        self.root = node
        return
    
    def operate(self, node, func, val, val2):
        '''find value in the B tree if present else return -1'''
        if node.is_leaf:
            # print(func, val)
            ret = node.operate(val, val2)
        else:
            if val < node.keys[0]:
                ret = self.operate(node.pointers[0], func, val, val2)
            for i in range(len(node.keys[:-1])):
                if node.keys[i] <= val and val < node.keys[i+1]:
                    ret = self.operate(node.pointers[i+1], func, val, val2)
                    ind = i+1
            if node.keys[-1] <= val:
                ret = self.operate(node.pointers[-1], func, val, val2)
        return ret

    def print(self):
        '''print the btree level wise'''
        arr = [self.root, None]
        i = 0
        while i < len(arr):
            if arr[i] is None:
                print('\n')
                arr.append(None)
            else:
                arr[i].print()
                for pointer in arr[i].pointers:
                    arr.append(pointer)
            # del(arr[i])
            i += 1
            if arr[-1] == arr[-2] == None:
                break
