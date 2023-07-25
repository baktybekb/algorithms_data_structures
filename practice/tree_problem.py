class Node:
    def __init__(self, name, salary, children):
        self.name = name
        self.salary = salary
        self.children: list = children


class TreeInfo:
    def __init__(self):
        self.number_of_unpaid_managers = 0


def main(root):
    tree_info = TreeInfo()
    helper(root, tree_info)
    return tree_info.number_of_unpaid_managers


# O(n) time | O(d) space, d --> depth of the tree, recursive call stack
def helper(node, tree_info):
    if len(node.children) == 0:
        return node.salary, 0

    total_child_salary = 0
    total_child_number = len(node.children)

    for child in node.children:
        salary, child_number = helper(child, tree_info)
        total_child_salary += salary
        total_child_number += child_number

    average = total_child_salary / total_child_number
    if node.salary < average:
        tree_info.number_of_unpaid_managers += 1
    return total_child_salary + node.salary, total_child_number


if __name__ == '__main__':
    #  A
    # B C
    #    D
    node_d = Node(name='D', salary=60, children=[])
    node_c = Node(name='C', salary=200, children=[node_d])
    node_b = Node(name='B', salary=100, children=[])
    node_a = Node(name='A', salary=100, children=[node_b, node_c])
    assert main(node_a) == 1

    # A
    node_a = Node(name='A', salary=100, children=[])  # only root
    assert main(node_a) == 0

    #   A
    # B C D
    node_d = Node(name='D', salary=100, children=[])
    node_c = Node(name='C', salary=100, children=[])
    node_b = Node(name='B', salary=100, children=[])
    node_a = Node(name='A', salary=100, children=[node_b, node_c, node_d])
    assert main(node_a) == 0

    #   A
    # B C D
    node_d = Node(name='D', salary=111, children=[])
    node_c = Node(name='C', salary=100, children=[])
    node_b = Node(name='B', salary=100, children=[])
    node_a = Node(name='A', salary=100, children=[node_b, node_c, node_d])
    assert main(node_a) == 1

    #  A
    # B C
    #    D
    node_d = Node(name='D', salary=400, children=[])
    node_c = Node(name='C', salary=200, children=[node_d])
    node_b = Node(name='B', salary=100, children=[])
    node_a = Node(name='A', salary=100, children=[node_b, node_c])
    assert main(node_a) == 2
