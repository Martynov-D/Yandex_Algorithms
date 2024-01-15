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


def find_min(root: list, tree: list) -> int:
    """
    Finds the minimum key in the given tree

    :param root: root of the tree
    :param tree: tree to search through
    :return: index of the minimum element
    """

    pointer = root
    while pointer is not None:
        if pointer[1] is None:
            return pointer[4]
        else:
            pointer = tree[0][pointer[1]]


def find_max(root: list, tree: list) -> int:
    """
    Finds the maximum key in the given tree

    :param root: root of the tree
    :param tree: tree to search through
    :return: index of the maximum element
    """

    pointer = root
    while pointer is not None:
        if pointer[2] is None:
            return pointer[4]
        else:
            pointer = tree[0][pointer[2]]


def find_second_max(root: list, tree: list) -> int:
    if root[2] is None:
        return tree[0][find_max(tree[0][root[1]], tree)][0]
    else:
        max_node = find_max(tree[0][root[2]], tree)
        if tree[0][max_node][1] is None:
            return tree[0][tree[0][max_node][3]][0]
        else:
            return tree[0][find_max(tree[0][tree[0][max_node][1]], tree)][0]


def inorder_traversal(root: list, tree: list):
    if root[1] is not None:
        inorder_traversal(tree[0][root[1]], tree)
    print(root[0])
    if root[2] is not None:
        inorder_traversal(tree[0][root[2]], tree)


def inorder_leaves_traversal(root: list, tree: list):
    if root[1] is None and root[2] is None:
        print(root[0])
        return
    if root[1] is not None:
        inorder_leaves_traversal(tree[0][root[1]], tree)
    if root[2] is not None:
        inorder_leaves_traversal(tree[0][root[2]], tree)


def inorder_full_parent_traversal(root: list, tree: list):
    if root[1]:
        inorder_full_parent_traversal(tree[0][root[1]], tree)
    if root[1] and root[2]:
        print(root[0])
    if root[2]:
        inorder_full_parent_traversal(tree[0][root[2]], tree)


def inorder_branch_traversal(root: list, tree: list):
    if root[1]:
        inorder_branch_traversal(tree[0][root[1]], tree)
    if (not root[1]) is not (not root[2]):
        print(root[0])
    if root[2]:
        inorder_branch_traversal(tree[0][root[2]], tree)


def count_height(root: list, tree: list) -> int:
    h1 = 0
    h2 = 0
    if root[1]:
        h1 = count_height(tree[0][root[1]], tree)
    if root[2]:
        h2 = count_height(tree[0][root[2]], tree)
    root[5] = max(h1, h2) + 1
    if abs(h1 - h2) > 1:
        tree[2] = False
    return root[5]


def main():
    numbers = list(map(int, input().split()))
    tree = allocate_memory(len(numbers) - 1)

    root = tree[0][0]
    root[0] = numbers[0]
    tree[1] += 1

    for key in numbers[1:-1]:
        fill_node(root, key, tree)
    inorder_branch_traversal(root, tree)

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    main()
