def buildnextline(prevline):
    nextLine = [0] * (2 * len(prevLine))
    for i in range(len(nextLine)):
        #calculate the index of the parent
        parentIndex = i / 2

        #if the node is at an even index then it is a left child
        isNodeLeftSib = (i % 2 == 0)

        #calculate the index of the respective sibling of the parent
        if isNodeLeftSib:
            parentSiblingIndex = parentIndex - 1
        else:
        parentSiblingIndex = parentIndex + 1
    return 0