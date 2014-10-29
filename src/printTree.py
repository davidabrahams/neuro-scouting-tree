import sys

#read the number of layers the tree will have from the input argument
layers = int(sys.argv[1])

#initialize the tree and set the starting node
tree = [None] * layers
if layers > 0:
    tree[0] = [1]

#generate the tree
for i in range(1, layers):
    tree[i] = [1] * (2 * len(tree[i - 1]))

#print the tree
print(tree)