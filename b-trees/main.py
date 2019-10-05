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
            val = int(line[1])
            ret, new_key, new_node = btree.insert(btree.root, val)
            btree.change_root(ret, new_key, new_node)
            btree.print()
        
        elif line[0] == 'FIND':
            val = int(line[1])
            btree.find(val)

        elif line[0] == 'COUNT':
            val = int(line[1])
            btree.count(val)

        elif line[0] == 'RANGE':
            x = int(line[1])
            y = int(line[2])
            btree.range(x, y)
