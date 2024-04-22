def tree_by_levels(node):
    if node is None:
        return []
    fin = []
    order = []
    order.append(node)
    while order:
        count = len(order)
        while count > 0:
            curr = order.pop(0)
            fin.append(curr.value)
            if curr.left:
                order.append(curr.left)
            if curr.right:
                order.append(curr.right)
            count -= 1
    return fin
