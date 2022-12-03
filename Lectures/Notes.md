## Лекция 2: линейный поиск

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

## Лекция 3: 