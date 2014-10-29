neuro-scouting-tree
===================

- Running the script -
Run printTree.py

- Code organization -

printTree.py: a script prompts the user for how many layers to generate for the tree, as well as the tree's initial node. It then generates and prints the requested tree layer by layer to the console using the build_tree and print_tree functions in the treeBuilder module.

treeBuilder.py: a module containing the following methods for generating and printing a tree
-print_tree(tree): prints the tree layer to the console
-build_tree(layers, first_node): builds a tree layer by layer using the function next_layer(prev_layer)
-next_layer(prev_layer): builds the next layer of the tree so that each left child is the sum of the parent and the parent's left sibling, and each right child is the sum of the parent and the parent's right sibling.

- Optimizations -

The tree is built layer by layer rather than node by node, as it allows for quicker and more efficient identification of parent siblings.

All lists are pre-allocated for speed.

While looping through prev_layer to generate next_layer, only one list look-up is performed to create every two children, as the parent and its right_sib node are remembered from the previous iteration and then stored in left_sib and parent, respectively.


