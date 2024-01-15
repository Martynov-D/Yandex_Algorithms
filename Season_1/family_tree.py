import sys


def allocate_memory(max_nodes: int) -> list:
    """
    Allocates memory for binary tree of fixed capacity.

    :param max_nodes: capacity of the tree
    :return: [[allocated memory], index of the first empty element, is balanced or not]
    """

    memory = list()
    for i in range(max_nodes):
        # key, left, right, parent, index, height of subtree
        memory.append([None, None, None, None, i, 1])
    return [memory, 0, True]


def fill_node(root: list, key: int, tree: list):
    """
    Fills in node of the given tree with the given key

    :param root: root of the given tree
    :param key: value to add to the tree
    :param tree: tree to add key to
    """

    pointer = root
    prev_node = [0, 'o']

    while pointer is not None:
        prev_node[0] = pointer[4]
        if key < pointer[0]:
            prev_node[1] = 'l'
            pointer = tree[0][pointer[1]] if pointer[1] is not None else None
        elif key > pointer[0]:
            prev_node[1] = 'r'
            pointer = tree[0][pointer[2]] if pointer[2] is not None else None
        else:
            return

    tree[0][tree[1]][0] = key
    tree[0][tree[1]][3] = prev_node[0]

    match prev_node[1]:
        case 'l':
            tree[0][prev_node[0]][1] = tree[1]
        case 'r':
            tree[0][prev_node[0]][2] = tree[1]
    tree[1] += 1


def inorder_traversal(root: list, tree: list, family_tree: dict):
    if root[1] is not None:
        inorder_traversal(tree[0][root[1]], tree, family_tree)
    print(root[0], family_tree[root[0]]['height'])
    if root[2] is not None:
        inorder_traversal(tree[0][root[2]], tree, family_tree)


def count_children(name: str, tree: dict):
    if tree[name]['children']:
        for child in tree[name]['children']:
            tree[name]['offspring'] += (count_children(child, tree) + 1)
    return tree[name]['offspring']


def count_height(name: str, tree: dict, height: int):
    tree[name]['height'] = height
    for child in tree[name]['children']:
        count_height(child, tree, height + 1)


def find_family_root(tree: dict):
    family_root = next(iter(tree))
    for key, person in tree.items():
        if not person['parent']:
            family_root = key
    return family_root


def main():
    number_of_people = int(input())

    family_tree = dict()
    tree = allocate_memory(number_of_people)

    person, parent = input().split()
    root = tree[0][0]
    root[0] = parent
    tree[1] += 1
    fill_node(root, person, tree)

    family_tree[parent] = {'children': set(), 'parent': None, 'offspring': 0}
    family_tree[parent]['children'].add(person)
    family_tree[person] = {'children': set(), 'parent': parent, 'offspring': 0}

    for _ in range(2, number_of_people):
        person, parent = input().split()
        fill_node(root, parent, tree)
        fill_node(root, person, tree)

        if parent not in family_tree:
            family_tree[parent] = {'children': set(), 'parent': None, 'offspring': 0}
        if person not in family_tree:
            family_tree[person] = {'children': set(), 'parent': parent, 'offspring': 0}
        family_tree[person]['parent'] = parent
        family_tree[parent]['children'].add(person)

    family_root = find_family_root(family_tree)
    count_children(family_root, family_tree)
    count_height(family_root, family_tree, 0)
    inorder_traversal(root, tree, family_tree)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    main()
