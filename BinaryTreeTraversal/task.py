# Pre-order traversal
def pre_order(node):
    order=[]
    if node:
        order.append(node.data)
        order.extend(pre_order(node.left))
        order.extend(pre_order(node.right))
    return order

# In-order traversal
def in_order(node):
    order = []
    if node:
        order.extend(in_order(node.left))
        order.append(node.data)
        order.extend(in_order(node.right))
    return order

# Post-order traversal
def post_order(node):
    order = []
    if node:
        order.extend(post_order(node.left))
        order.extend(post_order(node.right))
        order.append(node.data)
    return order
