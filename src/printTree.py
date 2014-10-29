from treeBuilder import build_tree

#prompt the user for the number of layers and the first node
layers = int(raw_input('How many layers would you like the tree to have? >>>'))
first_node = int(raw_input('What would you like the topmost value of the tree to be? >>>'))

#create the tree
tree = build_tree(layers, first_node)

#print the tree
print(tree)