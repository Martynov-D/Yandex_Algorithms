## Лекция 2: Линейный поиск

### Задача 7

Остров состоит из блоков 1х1. Прошел дождь и заполнил все ложбины. По ландшафту острова определите, сколько блоков воды
осталось в низинах после дождя

Решение: найти координаты самой высокой вершины. Потом пройти по левой и правой части относительно вершины. Пока идем,
обновляем локальную максимальную высоту пика и, если текущая позиция ниже локального пика, прибавляем разницу к сумме
блоков воды

```python
def isleflood(land):
    # index of the maximum height
    max_height = 0

    for i in range(1, len(land)):
        if land[i] > land[max_height]:
            max_height = i

    cur_max = 0
    total_water = 0
    # count number of water blocks to the left from max_height
    for i in range(max_height):
        if land[i] > cur_max:
            cur_max = land[i]
        total_water += cur_max - land[i]

    cur_max = 0
    # count number of water blocks to the right from max_height
    for i in range(len(land) - 1, max_height, -1):
        if land[i] > cur_max:
            cur_max = land[i]
        total_water += cur_max - land[i]

    return total_water
```

### Задача 8

Дана строка, возможно пустая, состоящая из букв A-Z. Нужно написать функцию RLE. Если на вход пришла неподходящая
строка, вывести ошибку.

```python
def rle(string):
    last_symbol = string[0]
    position = 0
    encoded = list()

    for i in range(1, len(string)):
        if string[i] != last_symbol:
            if i - position > 1:
                encoded.append(f'{last_symbol}{i - position}')
            else:
                encoded.append(f'{last_symbol}')
            last_symbol = string[i]
            position = i
        encoded.append(f'{last_symbol}{len(string) - position}')
    return ''.join(encoded)
```

## Лекция 3: Множество

Множество

```python
hashTableSize = 10
m_set = [[] for _ in range(hashTableSize)]


def count_hash(x):
    return x % hashTableSize


def add(x):
    if not find(x):
        m_set[count_hash(x)].append(x)


def find(x):
    for number in m_set[count_hash(x)]:
        if number == x:
            return True
    return False


def delete(x):
    x_list = m_set[count_hash(x)]
    for i in range(len(x_list)):
        if x_list[i] == x:
            x_list[i] = x_list[len(x_list) - 1]
            x_list.pop()
            return
```

## Лекция 5: Префиксные суммы и два указателя

### Задача 2

Найти количество отрезков последовательности чисел с нулевой суммой. Например, найти количество промежутков времени, когда ЗП погашала траты.

Простое решение за $O(nˆ3)$: перебираем левую и правую границы интервала всеми возможными способами, и циклом проходим по интервалу, считая сумму.

```python
def n3(array):
    ranges = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array) + 1):
            r_sum = 0
            for k in range(i, j):
                r_sum += array[k]
            if r_sum == 0:
                ranges += 1
    return ranges
```

Решение за $O(nˆ2)$: перебираем левую и правую границы, но не пересчитываем сумму, а накапливаем. Когда она равна нулю, прибавляем к счетчику единицу.

```python
def n2(array):
    ranges = 0
    for i in range(len(array)):
        r_sum = 0
        for j in range(i, len(array)):
            r_sum += array[j]
            if r_sum == 0:
                ranges += 1
    return ranges
```

Линейное решение: 
1. Cчитаем префиксные суммы. 
2. Считаем количество вхождений одинаковых значений префиксной суммы. Между одинаковыми значениями сумма будет равна нулю.
3. При помощи комбинаторики суммируем для всех значений префиксных сумм количество интервалов с нулевой суммой.

```python
# Стандартная функция для подсчета префиксных сумм
def countPrefix(array):
    prefix = [0] * (len(array) + 1)
    for i in range(1, len(array) + 1):
        prefix[i] = prefix[i-1] + array[i - 1]

    return prefix


def n(array):
    prefix = countPrefix(array)
    prefixes = dict()
    for element in prefix:
        if element not in prefixes:
            prefixes[element] = 0
        prefixes[element] += 1

    ranges = 0
    for r in prefixes.values():
        ranges += r * (r - 1) // 2
    return ranges
```

### Задача 4

Игроки характеризуются профессианализмом, который выражается числовой характеристикой. Требуется найти максимальный суммарный профессианализм сплоченой команды. Команда сплоченая, когда самый сильный игрок не лучше двух самых слабых.

```python
def best_professional_team(players):
    best_sum = 0 
    cur_sum = 0
    last_player = 0
    for first_player in range(len(players)):
        while last_player < len(players) and (players[last_player] <= players[first_player] + players[first_player + 1]) # or last_player == first_player)
            cur_sum += players[last_player]
            last_player += 1
        best_sum = max(best_sum, cur_sum)
        cur_sum -= players[first_player]
    return best_sum
```

### Слияние двух отсортированных списков
```python
def merge(arr1, arr2):
    merged = [0] * (len(arr1) + len(arr2))
    first = 0
    second = 0
    for k in range(len(merged)):
        if first < len(arr1) and (second == len(arr2) or arr1[first] < arr2[second]): 
            merged[k] = arr1[first]
            first += 1
        else:
            merged[k] == arr2[second]
            second += 1
    return merged
```

## Лекция 6: Бинарный поиск

### Левый бинарный поиск (поиск первого хорошего)

```python
def lBinSearch(l, r, check, *args):
    while l < r:
        # Тоже самое, что (l + r) // 2
        m = l + (r - l) // 2
        if check(m, args):
            r = m
        else:
            l = m + 1
    return l
```

### Правый бинарный поиск (поиск последнего хорошего)

```python
def rBinSearch(l, r, check, *args):
    while l < r:
        # Тоже самое, что (l + r + 1) // 2
        m = l + (r - l + 1) // 2
        if check(m, args):
            l = m
        else:
            r = m - 1
    return l
```

### Вещественный бинарный поиск

```python
def fBinSearch(l, r, eps, check, *args):
    while l + eps < r:
        m = l + (r - l) / 2
        if check(m, args):
            r = m
        else:
            l = m
    return l
```

## Лекция 8: Бинарное дерево

### Свой менеджер памяти

```python
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
```

### Дерево

```python
def find(mem_struct, root, x):
    key = mem_struct[0][root][0]
    if key == x:
        return root
    elif key > x:
        left = mem_struct[0][root][1]
        if left == -1:
            return -1
        else:
            return find(mem_struct, left, x)
    elif key < x:
        right = mem_struct[0][root][2]
        if right == -1:
            return -1
        else:
            return find(mem_struct, right, x)


def create_and_fill_node(mem_struct, key):
    index = create_node(mem_struct)
    mem_struct[0][index][0] = key
    mem_struct[0][index][1] = -1
    mem_struct[0][index][2] = -1
    return index


def add(mem_struct, root, x):
    key = mem_struct[0][root][0]
    if key > x:
        left = mem_struct[0][root][1]
        if left == -1:
            mem_struct[0][root][1] = create_and_fill_node(mem_struct, x)
        else:
            add(mem_struct, left, x)
    elif key < x:
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
```

### Дерево Хаффмана

```python
def make_tree(serialized):
    tree = {'left': None, 'right': None, 'up': None, 'type': 'root'}
    current_node = tree
    for symbol in serialized:
        if symbol == 'D':
            new_node = {'left': None, 'right': None, 'up': current_node, 'type': 'left'}
            current_node['left'] = new_node
            current_node = new_node
        elif symbol == 'U':
            while current_node['type'] == 'right':
                current_node = current_node['up']
            current_node = current_node['up']
            new_node = {'left': None, 'right': None, 'up': current_node, 'type': 'right'}
            current_node['right'] = new_node
            current_node = new_node
    return tree

def traverse(root, prefix):
    if root['left'] is None and root['right'] is None:
        return [''.join(prefix)]
    prefix.append('0')
    ans = traverse(root['left'], prefix)
    prefix.pop()
    prefix.append('1')

    ans.extend(traverse(root['right'], prefix))
    prefix.pop()
    return ans

# D - перейти к левому ребенку, U - поднимайся наверх, пока можешь, потом перейди к правому ребенку
tree = make_tree('DUDU')
codes = traverse(tree, [])
```

## Лекция 11: Динамическое программирование с одним параметром

### Представление числа

Представить число N (до 10000) в виде арифметического выражения с наименьшим количеством символов, в котором используются число до К, операции сложения, умножения и скобки

```python

```