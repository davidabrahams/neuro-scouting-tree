def next_line(prev_layer):
    """
    @param prev_layer: the previous line in the tree
    @return: next_layer: the next layer in the tree, computed based on the previous layer
    """

    #initialize the return variable
    next_layer = [0] * (2 * len(prev_layer))

    #calculate the values of all the nodes in the next layer
    for i in range(len(next_layer)):
        #calculate the index of the parent
        parent_index = i / 2

        #if the node is at an even index then it is a left child
        node_left = (i % 2 == 0)

        #calculate the index of the respective sibling of the parent
        if node_left:
            parent_sib_index = parent_index - 1
        else:
            parent_sib_index = parent_index + 1

        #calculate the new node in the tree
        node = prev_layer[parent_index]
        if (parent_sib_index > 0) and (parent_sib_index < len(prev_layer)):
            node += prev_layer[parent_sib_index]

        #place the node in the next layer
        next_layer[i] = node

    return next_layer

#test the next_line function, output should be [1, 3, 2, 4, 4, 3, 3, 1]
test_layer = [1, 2, 2, 1]
next_layer = next_line(test_layer)
print next_layer