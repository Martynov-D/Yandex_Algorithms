def init_memory(max_capacity):
    memory = list()
    for i in range(max_capacity):
        memory.append([0, i + 1, 0])
    return [memory, 0]


def create_node(mem_struct):
    memory, first_empty = mem_struct
    mem_struct[1] = memory[first_empty][1]
    return first_empty


def delete_node(mem_struct, index):
    memory, first_empty = mem_struct
    memory[index][1] = first_empty
    mem_struct[1] = index


def create_and_fill_node(mem_struct, key):
    index = create_node(mem_struct)
    mem_struct[0][index][0] = key
    mem_struct[0][index][1] = -1
    mem_struct[0][index][2] = -1
    return index


def add(mem_struct, root, x):
    key = mem_struct[0][root][0]
    if x < key:
        left = mem_struct[0][root][1]
        if left == -1:
            mem_struct[0][root][1] = create_and_fill_node(mem_struct, x)
        else:
            add(mem_struct, left, x)
    elif x > key:
        right = mem_struct[0][root][2]
        if right == -1:
            mem_struct[0][root][2] = create_and_fill_node(mem_struct, x)
        else:
            add(mem_struct, right, x)


def main():
    numbers = list(map(int, input().split()))
    tree = init_memory(len(numbers) - 1)
    root = create_and_fill_node(tree, numbers[0])

    for i in numbers[1:-1]:
        add(tree, root, i)

    print(tree)


if __name__ == '__main__':
    main()
