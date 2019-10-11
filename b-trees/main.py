import os
import sys
from node import Node
from btree import Btree

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('format python3 main.py FILENAME')
        exit(0)
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print('"{}" file is not present'.format(filename))
        exit(0)
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    # create a Btree object
    btree = Btree()

    for line in lines:
        line = line.strip().split(' ')
        if line[0] == 'INSERT':
            val = float(line[1])
            ret, new_key, new_node = btree.insert(btree.root, val)
            btree.change_root(ret, new_key, new_node)
        
        elif line[0] == 'FIND':
            val = float(line[1])
            ret = btree.operate(btree.root, 'find', val, val)
            if ret == 0:
                print('NO')
            elif ret:
                print('YES')

        elif line[0] == 'COUNT':
            val = float(line[1])
            ret = btree.operate(btree.root, 'count', val, val)
            print(ret)

        elif line[0] == 'RANGE':
            x = float(line[1])
            y = float(line[2])
            ret = btree.operate(btree.root, 'range', x, y)
            print(ret)

    # btree.print()
