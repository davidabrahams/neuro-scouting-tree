def next_line(prev_layer):
    """
    @param prev_layer: the previous line in the tree
    @return: next_layer: the next layer in the tree, computed based on the previous layer
    """

    next_layer = [0] * (2 * len(prev_layer))

    #parent is the current parent node, left_sib and right_sib are the parent's siblings
    parent = 0
    right_sib = prev_layer[0]

    #loop through the parent layer, stopping before the final node
    for i in range(len(prev_layer) - 1):

        left_sib = parent #the previously examined parent becomes the left sibling
        parent = right_sib #the previous right_sibling becomes the parent
        right_sib = prev_layer[i + 1] #get the new right_sibling from the list

        #generate the parent's children
        next_layer[2 * i] = parent + left_sib
        next_layer[2 * i + 1] = parent + right_sib

    #the final parent is a special case where the right sibling does not exist
    left_sib = parent
    parent = right_sib
    right_sib = 0

    #generate the final pair of children
    next_layer[len(next_layer) - 2] = parent + left_sib
    next_layer[len(next_layer) - 1] = parent + right_sib

    return next_layer


def build_tree(layers, first_node):
    """
    @param layers: the number of layers the tree contains
    @param first_node: the top node in the tree
    @return: a list where each element is a list containing the nodes in a layer of the tree
    """
    #initialize the tree
    tree = [None] * layers

    #set the top node
    if layers > 0:
        tree[0] = [first_node]

    #loop through computing each layer of the tree based on the previous layer
    for i in range(0, layers - 1):
        tree[i + 1] = next_line(tree[i])

    return tree


def print_tree(tree):
    """
    prints a tree with the given number of layers and first node
    @param layers: the number of layers the tree contains
    @param first_node: the top node in the tree
    """
    for layer in tree:
        print layer