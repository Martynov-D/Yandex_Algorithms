Link: <https://contest.yandex.ru/contest/28724/enter/>

## A

Решить в целых числах уравнение ( ax + b ) : ( cx + d ) = 0

### Формат ввода

Вводятся 4 числа: a, b, c и d; c и d не равны нулю одновременно.

### Формат вывода

Необходимо вывести все целочисленные решения, если их число конечно, “NO” (без кавычек), если целочисленных решений нет,
и “INF” (без кавычек), если их бесконечно много.

<i>Example 1:</i>

| In               | Out |
|------------------|-----|
| 1<br>1<br>2<br>2 | NO  |

<i>Example 2:</i>

| In                | Out |
|-------------------|-----|
| 2<br>-4<br>7<br>1 | 2   |

<i>Example 3:</i>

| In                   | Out |
|----------------------|-----|
| 35<br>14<br>11<br>-3 | NO  |

```python
# TODO let me out
```

## B

На уроке геометрии семиклассники Вася и Петя узнали, что такое параллелограмм. На перемене после урока они стали играть
в игру: Петя называл координаты четырех точек в произвольном порядке, а Вася должен был ответить, являются ли эти точки
вершинами параллелограмма.

Вася, если честно, не очень понял тему про параллелограммы, и ему требуется программа, умеющая правильно отвечать на
Петины вопросы.

Напомним, что параллелограммом называется четырехугольник, противоположные стороны которого равны и параллельны.

### Формат ввода

В первой строке входного файла записано целое число N (1 ≤ N ≤ 10) - количество заданных Петей вопросов. Каждая из N
последующих строк содержит описание четырех точек - четыре пары целых чисел X и Y (−100 ≤ X ≤ 100, −100 ≤ Y ≤ 100),
обозначающих координаты точки. Гарантируется, что четыре точки, о которых идет речь в одном вопросе, не лежат на одной
прямой.

### Формат вывода

Для каждого из вопросов выведите "YES", если четыре заданные точки могут образовать параллелограмм, и "NO" в противном
случае. Ответ на каждый из запросов должен быть в отдельной строке без кавычек.

<i>Example 1:</i>

| In                                                         | Out              |
|------------------------------------------------------------|------------------|
| 3<br>1 1 4 2 3 0 2 3<br>1 1 5 2 2 3 3 0<br>0 0 5 1 6 3 1 2 | YES<br>NO<br>YES |

```python
def make_vector(a, b):
    return b[0] - a[0], b[1] - a[1]


# from itertools built in library with few changes
def combinations(iterable, r, points: dict):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    temp = tuple(pool[i] for i in indices)
    yield temp, make_vector(points[temp[0]], points[temp[1]])
    # yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        # yield tuple(pool[i] for i in indices)
        temp = tuple(pool[i] for i in indices)
        yield temp, make_vector(points[temp[0]], points[temp[1]])


def count_length(vectors: dict):
    for key, value in vectors.items():
        length = value[0] ** 2 + value[1] ** 2
        yield key, length


def check_figures(vectors: dict, vectors_lengths: dict):
    # all possible pairs of vectors without intersection of their points
    # AB, CD or AC, BD or AD, BC
    # indices = [(0, 5), (1, 4), (2, 3)]
    keys = list(vectors.keys())
    values = list(vectors.values())

    for i in range(3):
        # indices list can be used here in cases where a few points are given
        v1 = values[i]
        v2 = values[len(values) - 1 - i]

        if vectors_lengths[keys[i]] == vectors_lengths[keys[len(keys) - 1 - i]]:
            det = v1[0] * v2[1] - v1[1] * v2[0]
            if det == 0:
                print('YES')
                return
    print('NO')


def main():
    number_of_question = int(input())
    for _ in range(number_of_question):
        # points on linear space
        x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
        points = {'a': (x1, y1),
                  'b': (x2, y2),
                  'c': (x3, y3),
                  'd': (x4, y4)}

        # all possible vectors
        vectors = {key: value for key, value in combinations(points.keys(), 2, points)}
        vectors_lengths_squared = {key: value for key, value in count_length(vectors)}

        check_figures(vectors, vectors_lengths_squared)
```

## C

Напишите программу, которая по изображению поля для игры в «Крестики-нолики» определит, могла ли такая ситуация
возникнуть в результате игры с соблюдением всех правил.

Напомним, что игра в «Крестики-нолики» ведется на поле 3*3. Два игрока ходят по очереди. Первый ставит крестик, а второй
– нолик. Ставить крестик и нолик разрешается в любую еще не занятую клетку поля. Когда один из игроков поставит три
своих знака в одной горизонтали, вертикали или диагонали, или когда все клетки поля окажутся заняты, игра заканчивается.

### Формат ввода

Вводится три строки по три числа в каждой, описывающих игровое поле. Число 0 обозначает пустую клетку, 1 – крестик, 2 –
нолик. Числа в строке разделяются пробелами.

### Формат вывода

Требуется вывести слово YES, если указанная ситуация могла возникнуть в ходе игры, и NO в противном случае.

<i>Example 1:</i>

| In                       | Out |
|--------------------------|-----|
| 1 1 1<br> 1 1 1<br>1 1 1 | NO  |

<i>Example 2:</i>

| In                      | Out |
|-------------------------|-----|
| 2 1 1<br>1 1 2<br>2 2 1 | YES |

<i>Example 3:</i>

| In                      | Out |
|-------------------------|-----|
| 1 1 1<br>2 0 2<br>0 0 0 | YES |

<i>Example 4:</i>

| In                      | Out |
|-------------------------|-----|
| 0 0 0<br>0 1 0<br>0 0 0 | YES |

```python

def main():
    # Keyboard input
    field = list()
    for _ in range(3):
        field.append(input().split())

    # Test matrix
    # field = [
    #     ['2', '2', '1'],
    #     ['2', '1', '1'],
    #     ['0', '2', '1']
    # ]

    first_won = False
    second_won = False
    ones = 0
    twos = 0
    # Count total amount of ones and twos and check for horizontal lines '1 1 1' or '2 2 2'
    for line in field:
        cur_ones = 0
        cur_twos = 0
        for element in line:
            match element:
                case '0':
                    pass
                case '1':
                    cur_ones += 1
                case '2':
                    cur_twos += 1
            # print(element, end=' ')
        if cur_ones == 3:
            first_won = True
        if cur_twos == 3:
            second_won = True
        ones += cur_ones
        twos += cur_twos
        # print()

    # Check for vertical lines '1 1 1' or '2 2 2'
    for line in [[line[0] for line in field], [line[1] for line in field], [line[2] for line in field]]:
        cur_ones = 0
        cur_twos = 0
        for element in line:
            match element:
                case '0':
                    pass
                case '1':
                    cur_ones += 1
                case '2':
                    cur_twos += 1
        if cur_ones == 3:
            first_won = True
        if cur_twos == 3:
            second_won = True

    # Check the main diagonal
    cur_ones = 0
    cur_twos = 0
    for i in range(3):
        match field[i][i]:
            case '1':
                cur_ones += 1
            case '2':
                cur_twos += 1

    if cur_ones == 3:
        first_won = True
    if cur_twos == 3:
        second_won = True

    # Check the anti-diagonal
    cur_ones = 0
    cur_twos = 0
    for i in range(3):
        match field[i][2 - i]:
            case '1':
                cur_ones += 1
            case '2':
                cur_twos += 1

    if cur_ones == 3:
        first_won = True
    if cur_twos == 3:
        second_won = True

    possible = 'YES'
    impossible = 'NO'

    difference = ones - twos
    # print(f'ones: {ones}, twos: {twos}, difference: {difference}, first_won: {first_won}, second_won: {second_won}')
    if (first_won and second_won) or (difference < 0 or abs(difference) > 1) or (second_won and difference == 1) or (
            first_won and difference == 0):
        return impossible
    else:
        return possible
```

## D

С помощью изобретенной профессором машины Фарнсворт и Эми меняются телами с целью осуществить свои мечты: профессор
жаждет острых ощущений, а Эми мечтает есть от пуза, не опасаясь за фигуру. Впоследствии выясняется, что обмен разумом
между двумя телами возможен не более одного раза, и чтобы вернуться обратно в свои тела нужно произвести промежуточный
обмен. Бендер предлагает свою помощь, однако, заполучив тело Эми, он тут же скрывается, чтобы под чужой личиной украсть
корону императора Робо-Венгрии.

Эми, недовольная возможностями профессорского тела в плане обжорства, уговаривает поменяться Лилу. Фрай приходит в ужас.
Лила обижена и обвиняет Фрая в том, что его заботит только ее внешность. Фрай в отместку меняется телами с Зойдбергом.

Бендер оказывается пойман при попытке ограбления, однако освобождается, убедив императора в том, что он - робот в теле
человека. Узнав, что император втайне мечтает пожить немного жизнью простых людей, Бендер предлагает тому на время
поменяться телами. Но так как Профессор уехал рисковать жизнью в теле Бендера, пришлось подсунуть императору вместо
своего корпуса автоматизированное помойное ведро.

Фрай в теле Зойдберга и Лила в теле Профессора встречаются в ресторане, чтобы выяснить отношения. В конце концов они
понимают, что любят друг друга вовсе не за внешность. При виде сцены их бурного примирения Эми, на этот раз уже в теле
Гермеса, надолго теряет аппетит.

Бендер, поменявшись телами с правителем Робо-Венгрии, наслаждается жизнью на его яхте. Однако именно в этот вечер
заговорщики совершают покушение на императора. Жизнь Бендеру спасает появление профессора Фарнсворта.

После того, как все герои решают свои личные проблемы, профессору с помощью Бубльгума Тэйта и Сладкого Клайда из
команды "Ударники" удается вернуть всех в свои тела.

"Футурама". Десятый эпизод шестого сезона.

В очередной серии Футурамы было проведено несколько обменов разумами между телами героев,но, по крайней мере Бубльгум
Тэйт и Сладкий Клайд в обменах не участвовали. Теперь необходимо вернутьразумы всех героев в свои тела. К сожалению, два
тела могут участвовать только в одном обмене,поэтому обратные обмены для этого произвести невозможно. Например, если
тело 1поменялось разумом с телом 2, а потом тело 1 поменялось разумом с телом 3,то в теле 1 находится разум третьего
героя, в теле 2 - разум первого героя,а в теле 3 - второго.Теперь можно произвести обмен разумами только между телами 2
и 3, тогда разум второго героявернется в свое тело, а первому и третьему героям могут помочь только Тэйт с Клайдом.

Помогите героям Футурамы вернуться в свои тела.

### Формат ввода

Во входном файле записаны целые числа N (4 ≤ N ≤ 20) и M(1 ≤ M ≤ 100) - количество героев Футурамы и количество
произведенных обменов разумами.Герои занумерованы числами от 1 до N, изначально разум каждого из героев находится в
своем теле. В последующих M строчках записана последовательность совершенных обменов разумами. Каждый обмен описывается
двумя различными числами - номерами тел, которые, в этом обмене меняются разумами. Бубльгум Тэйт и Сладкий Клайд, как
наиболее разумные герои, имеют номера N−1 и N, и гарантируется, что в исходных обменах они не участвовали.

### Формат вывода

Выведите план обменов для возвращения разумов героев в свои телав виде пар различных чисел - номеров тел которые
участвовали в соответствующем обмене.Причем никакие два тела не должны обмениваться между собой разумами более одного
раза,включая исходные обмены. Если обменов не требуется, то можно ничего не выводить.Если планов обменов несколько, то
выведите любой из них (не обязательно минимальный).

Вернуть разумы героев в свои тела всегда возможно.

<i>Example 1:</i>

| In         | Out                             |
|------------|---------------------------------|
| 4 1<br>1 2 | 1 3<br>2 4<br>1 4<br>2 3<br>3 4 |

<i>Example 2:</i>

| In         | Out                             |
|------------|---------------------------------|
| 5 1<br>1 2 | 1 4<br>2 5<br>1 5<br>2 4<br>4 5 |

```python
def swap_minds(a: int, b: int, array: list):
    print(a, b)
    array[a], array[b] = array[b], array[a]
    return array[b]


def main():
    number_of_people, number_of_swaps = map(int, input().split())
    people = list(i for i in range(number_of_people + 1))
    for i in range(number_of_swaps):
        p1, p2 = map(int, input().split())
        people[p1], people[p2] = people[p2], people[p1]

    for i in range(1, number_of_people - 1):
        # find the first person with foreign mind
        if people[i] != i:
            temp = i
            while people[temp] != i:
                temp = swap_minds(temp, number_of_people - 1, people)
            temp = swap_minds(temp, number_of_people, people)
            swap_minds(temp, number_of_people, people)
            swap_minds(people[number_of_people - 1], number_of_people - 1, people)
    if people[number_of_people - 1] == number_of_people:
        swap_minds(number_of_people - 1, number_of_people, people)
```

## E

Среди треугольников периметра P с целыми длинами сторон найдите треугольник наибольшей и наименьшей ненулевой площади.

### Формат ввода

Входные данные содержат одно целое число P — периметр треугольника (3 ≤ P ≤ 10<sup>9</sup>).

### Формат вывода

В первой строке выведите три целых числа — длины сторон треугольника с заданным периметром и наибольшей площадью. Во
второй строке выведите три целых числа — длины сторон треугольника с заданным периметром и наименьшей ненулевой
площадью. Если решений несколько, выведите любое. Если целочисленных треугольников заданного периметра не существует,
выведите -1.

<i>Example 1:</i>

| In  | Out            |
|-----|----------------|
| 3   | 1 1 1<br>1 1 1 |

<i>Example 2:</i>

| In  | Out |
|-----|-----|
| 4   | -1  |

```python
def main():
    perimetr = int(input())

    a = perimetr // 3
    b = (perimetr - a) // 2
    c = perimetr - a - b
    if a + b <= c:
        print(-1)
    else:
        print(a, b, c)
        if perimetr % 2 == 0:
            a = 2
        else:
            a = 1
        b = c = (perimetr - a) // 2
        print(a, b, c)
```