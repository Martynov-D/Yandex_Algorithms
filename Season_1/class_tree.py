class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key

    def __repr__(self):
        return str(self.key)


def create_node(root: Node, key: int, tree: list):
    pointer = root
    prev_node = [None, None]

    while pointer is not None:
        prev_node[0] = pointer
        if key < pointer.key:
            prev_node[1] = 'l'
            pointer = pointer.left
        elif key > pointer.key:
            prev_node[1] = 'r'
            pointer = pointer.right
        else:
            return

    temp = Node(key=key)
    temp.parent = prev_node[0]
    match prev_node[1]:
        case 'l':
            prev_node[0].left = temp
        case 'r':
            prev_node[0].right = temp

    tree.append(temp)


def find_node(root: Node, key: int):
    pass


def delete_node(root: Node, key: int):
    pass


def find_min(root: Node):
    pointer = root
    while pointer is not None:
        if pointer.left is None:
            return pointer
        else:
            pointer = pointer.left


def find_max(root: Node):
    pointer = root
    while pointer is not None:
        if pointer.right is None:
            return pointer
        else:
            pointer = pointer.right


def find_second_max(root: Node):
    if root.right is None:
        return find_max(root.left).key
    else:
        max_node = find_max(root.right)
        if max_node.left is None:
            return max_node.parent
        else:
            return max_node.left


# Solution from the Internet
def find_second_max_2(root: Node):
    pointer = root
    while pointer.right is not None:
        if pointer.right.right is None:
            return pointer.key
        pointer = pointer.right
    return pointer.left.key


def main():
    numbers = list(map(int, input().split()))
    root = Node(numbers[0])
    tree = [root]

    for i in numbers[1:-1]:
        create_node(root, i, tree)

    # for i in tree:
    #     print(f'{i.key} {i.left} {i.right} {i.parent}')

    print(find_second_max(root), find_second_max_2(root))


if __name__ == '__main__':
    main()
