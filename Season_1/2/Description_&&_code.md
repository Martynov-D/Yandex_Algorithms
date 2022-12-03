Link: <https://contest.yandex.ru/contest/27472/enter/>

## A

Дан список. Определите, является ли он монотонно возрастающим (то есть верно ли, что каждый элемент этого списка больше
предыдущего).

Выведите YES, если массив монотонно возрастает и NO в противном случае.

<i>Example :</i>

|  In   | Out  |
|:-----:|:----:|
| 1 7 9 | YES  |

<i>Example :</i>

|   In   | Out  |
|:------:|:----:|
| 1 9 7  |  NO  |

<i>Example :</i>

|   In   | Out  |
|:------:|:----:|
| 2 2 2  |  NO  |

```python
def main():
    numbers = list(map(int, input().split()))

    for i in range(1, len(numbers)):
        if numbers[i] <= numbers[i - 1]:
            return 'NO'
    return 'YES'
```

## B

По последовательности чисел во входных данных определите ее вид:

* CONSTANT – последовательность состоит из одинаковых значений
* ASCENDING – последовательность является строго возрастающей
* WEAKLY ASCENDING – последовательность является нестрого возрастающей
* DESCENDING – последовательность является строго убывающей
* WEAKLY DESCENDING – последовательность является нестрого убывающей
* RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов

### Формат ввода

По одному на строке поступают числа последовательности <i>ai, |ai| ≤ 10<sup>9</sup></i>.

Признаком окончания последовательности является число <i>-2 × 10<sup>9</sup></i>. Оно в последовательность не входит.

### Формат вывода

В единственной строке выведите тип последовательности.

<i>Example 1:</i>

|                              In                              |    Out     |
|:------------------------------------------------------------:|:----------:|
| -530<br>-530<br>-530<br>-530<br>-530<br>-530<br>-2000000000  |  CONSTANT  |

```python
def main():
    stop_number = -2e9
    numbers = list()
    number = int(input())
    while number != stop_number:
        numbers.append(number)
        number = int(input())

    ascending = False
    descending = False
    constant = False

    for i in range(len(numbers)):
        if numbers[i] > numbers[i + 1]:
            descending = True
        elif numbers[i] < numbers[i + 1]:
            ascending = True
        elif numbers[i] == numbers[i + 1]:
            constant = True

    if ascending and not descending and not constant:
        print('ASCENDING')
    elif not ascending and descending and not constant:
        print('DESCENDING')
    elif not ascending and not descending and constant:
        print('CONSTANT')
    elif ascending and not descending and constant:
        print('WEAKLY ASCENDING')
    elif not ascending and descending and constant:
        print('WEAKLY DESCENDING')
    else:
        print('RANDOM')
```

## C

Напишите программу, которая находит в массиве элемент, самый близкий по величине к данному числу.

### Формат ввода

В первой строке задается одно натуральное число N, не превосходящее 1000 – размер массива. Во второй строке содержатся N
чисел – элементы массива (целые числа, не превосходящие по модулю 1000). В третьей строке вводится одно целое число x,
не превосходящее по модулю 1000.

### Формат вывода

Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько, выведите любое из них.

<i>Example 1:</i>

|          In           |  Out  |
|:---------------------:|:-----:|
|  5<br>1 2 3 4 5<br>6  |   5   |

<i>Example 2:</i>

|         In          | Out |
|:-------------------:|:---:|
| 5<br>5 4 3 2 1<br>3 |  3  |

```python
def main():
    length = int(input())
    numbers = list(map(int, input().split()))
    num_to_find = int(input())

    smallest_difference = abs(num_to_find - numbers[0])
    ind = 0

    for i in range(1, length):
        temp = abs(numbers[i] - num_to_find)
        if temp < smallest_difference:
            smallest_difference = temp
            ind = i
    print(numbers[ind])
```

## D

Дан список чисел. Определите, сколько в этом списке элементов, которые больше двух своих соседей и выведите количество
таких элементов.

### Формат ввода

Вводится список чисел. Все числа списка находятся на одной строке.

### Формат вывода

<i>Example 1:</i>

|     In     | Out |
|:----------:|:---:|
| 1 2 3 4 5  |  0  |

<i>Example 2:</i>

|     In     | Out |
|:----------:|:---:|
| 5 4 3 2 1  |  0  |

<i>Example 3:</i>

|     In     | Out |
|:----------:|:---:|
| 1 5 1 5 1  |  2  |

```python
def main():
    numbers = list(map(int, input().split()))
    i = 1
    count = 0
    while i < len(numbers) - 1:
        if numbers[i - 1] < numbers[i] and numbers[i + 1] < numbers[i]:
            count += 1
            i += 2
        else:
            i += 1
    print(count)
```

## E

Соревнования по метанию коровьих лепешек проводятся в Пермском крае с 2009 года.

К сожалению, после чемпионата потерялись записи с фамилиями участников, остались только записи о длине броска в том
порядке, в котором их совершали участники.

Тракторист Василий помнит три факта:

1) Число метров, на которое он метнул лепешку, оканчивалось на 5
2) Один из победителей чемпионата метал лепешку до Василия
3) Участник, метавший лепешку сразу после Василия, метнул ее на меньшее количество метров

Будем считать, что участник соревнования занял k-е место, если ровно (k − 1) участников чемпионата метнули лепешку
строго дальше, чем он.

Какое максимально высокое место мог занять Василий?

### Формат ввода

Первая строка входного файла содержит целое число n — количество участников чемпионата по метанию лепешек <i>(3 ≤ n ≤
10<sub>5</sub>).</i>

Вторая строка входного файла содержит n положительных целых чисел, каждое из которых не превышает 1000, — дальность
броска участников чемпионата, приведенные в том порядке, в котором происходило метание.

### Формат вывода

Выведите самое высокое место, которое мог занять тракторист Василий. Если не существует ни одного участника чемпионата,
который удовлетворяет, описанным выше условиям, выведите число 0.

<i>Example 1:</i>

|           In            | Out |
|:-----------------------:|:---:|
| 7<br>10 20 15 10 30 5 1 |  6  |

<i>Example 2:</i>

|      In       | Out |
|:-------------:|:---:|
| 3<br>15 15 10 |  1  |

<i>Example 3:</i>

|      In       | Out |
|:-------------:|:---:|
| 3<br>10 15 20 |  0  |

```python
def main():
    length = int(input())
    results = list(map(int, input().split()))

    winner = results[0]
    answer = 0

    for i in range(1, length - 1):
        if results[i] > winner:
            winner = results[i]
            answer = 0
        elif results[i] % 10 == 5:
            if results[i] > results[i + 1]:
                answer = max(answer, results[i])
    results.sort(reverse=True)
    if answer:
        return results.index(answer) + 1
    return 0
```

## F

Последовательность чисел назовем симметричной, если она одинаково читается как слева направо, так и справа налево.
Например, следующие последовательности являются симметричными:

* 1 2 3 4 5 4 3 2 1
* 1 2 1 2 2 1 2 1

Вашей программе будет дана последовательность чисел. Требуется определить, какое минимальное количество и каких чисел
надо приписать в конец этой последовательности, чтобы она стала симметричной.

### Формат ввода

Сначала вводится число N — количество элементов исходной последовательности (1 ≤ N ≤ 100). Далее идут N чисел — элементы
этой последовательности, натуральные числа от 1 до 9.

### Формат вывода

Выведите сначала число M — минимальное количество элементов, которое надо дописать к последовательности. Потом M чисел,
которые надо дописать к последовательности.

<i>Example 1:</i>

| In                     | Out |
|:-----------------------|:----|
| 9<br>1 2 3 4 5 4 3 2 1 | 0   |

<i>Example 2:</i>

| In             | Out        |
|:---------------|:-----------|
| 5<br>1 2 1 2 2 | 3<br>1 2 1 |

<i>Example 3:</i>

| In             | Out          |
|:---------------|:-------------|
| 5<br>1 2 3 4 5 | 4<br>4 3 2 1 |

```python
def main():
    # Not used
    length = int(input())

    numbers = list(map(int, input().split()))

    tail_index = 0
    current_prefix_length = 0
    l = 0
    r = len(numbers) - 1
    left = r - l

    # Ищем симметричную подпоследовательность.
    # l и r будут указывать на центр симметрии. Он состоит либо из 2 символов, либо из одного 
    # tail_index будет равен длине хвоста, который нужно подставить в конец, чтобы из исходной последоваетльности сделать симметричную.
    while left > 0:
        current_prefix_length += 1
        if numbers[l] != numbers[r]:
            tail_index += current_prefix_length
            l += 1
            r = len(numbers) - 1
            current_prefix_length = 0
        else:
            l += 1
            r -= 1
        left = r - l

    print(tail_index)
    if tail_index:
        # reverse a list without creating a new one
        for i in range(tail_index - 1, -1, -1):
            print(numbers[i], end=' ')
```

## G

Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа, произведение которых максимально.
Выведите эти числа в порядке неубывания. Список содержит не менее двух элементов. Числа подобраны так, что ответ
однозначен.

Решение должно иметь сложность <i>O(n)</i>, где <i>n</i> - размер списка.

<i>Example :</i>

|    In     | Out |
|:---------:|:---:|
| 4 3 5 2 5 | 5 5 |

<i>Example :</i>

|     In      |  Out  |
|:-----------:|:-----:|
| -4 3 -5 2 5 | -5 -4 |

<i>Example :</i>

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        In                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |     Out     |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|:-----------:|
| 12288 -10075 29710 15686 -18900 -17715 15992 24431 6220 28403 -23148 18480 -22905 5411 -7602 15560 -26674 11109 -4323 6146 -1523 4312 10666 -15343 -17679 7284 20709 -7103 24305 14334 -12281 17314 26061 25616 17453 16618 -24230 -19788 21172 11339 2202 -22442 -20997 1879 -8773 -8736 5310 -23372 12621 -25596 -28609 -13309 -13 10336 15812 -21193 21576 -1897 -12311 -6988 -25143 -3501 23231 26610 12618 25834 -29140 21011 23427 1494 15215 23013 -15739 8325 5359 -12932 18111 -72 -12509 20116 24390 1920 17487 25536 24934 -6784 -16417 -2222 -16569 -25594 4491 14249 -28927 27281 3297 5998 6259 4577 12415 3779 -8856 3994 19941 11047 2866 -24443 -17299 -9556 12244 6376 -13694 -14647 -22225 21872 7543 -6935 17736 -2464 9390 1133 18202 -9733 -26011 13474 29793 -26628 -26124 27776 970 14277 -23213 775 -9318 29014 -5645 -27027 -21822 -17450 -5 -655 22807 -20981 16310 27605 -18393 914 7323 599 -12503 -28684 5835 -5627 25891 -11801 21243 -21506 22542 -5097 8115 178 10427 25808 10836 -11213 18488 21293 14652 12260 42 21034 8396 -27956 13670 -296 -757 18076 -15597 4135 -25222 -19603 8007 6012 2704 28935 16188 -20848 13502 -11950 -24466 5440 26348 27378 7990 -11523 -26393 | 29710 29793 |

```python
def O_nlogn():
    numbers = list(map(int, input().split()))

    numbers.sort()
    if abs(numbers[0]) * abs(numbers[1]) > numbers[-1] * numbers[-2]:
        print(numbers[0], numbers[1])
    else:
        print(numbers[-2], numbers[-1])


def O_n():
    numbers = list(map(int, input().split()))

    # first positive < second positive
    # abs(first negative) < abs(second negative)
    first_positive, second_positive = sorted(numbers[0:2])
    second_negative, first_negative = first_positive, second_positive

    for number in numbers[2:]:
        # if '+' sign == 1 else -1
        sign = (number > 0) - (number < 0)
        match sign:
            case 1:
                if number > second_positive:
                    first_positive = second_positive
                    second_positive = number
                elif number > first_positive:
                    first_positive = number
            case -1:
                if number < second_negative:
                    first_negative = second_negative
                    second_negative = number
                elif number < first_negative:
                    first_negative = number

    if first_positive * second_positive >= first_negative * second_negative:
        print(first_positive, second_positive)
    else:
        print(second_negative, first_negative)
```

| Задача  | Компилятор     | Сложность  | Вердикт  | Время  | Память   |
|:--------|:---------------|:-----------|:---------|:-------|:---------|
| G       | Python 3.10.1  | O(nLogn)   | OK       | 99ms   | 11.32Mb  |
| G       | Python 3.10.1  | O(n)       | OK       | 104ms  | 13.09Mb  |

## H

В данном списке из <i>n ≤ 10<sup>5</sup></i> целых чисел найдите три числа,произведение которых максимально.<br>
Решение должно иметь сложность <i>O(n)</i>, где n - размер списка.

Выведите три искомых числа в любом порядке.

<i>Example 1:</i>

|          In          |   Out   |
|:--------------------:|:-------:|
| 3 5 1 7 9 0 9 -3 10  | 10 9 9  |

<i>Example 2:</i>

|       In       |      Out       |
|:--------------:|:--------------:|
| -5 -30000 -12  | -5 -12 -30000  |

<i>Example 3:</i>

|   In   |  Out   |
|:------:|:------:|
| 1 2 3  | 3 2 1  |

```python
def nth_element(array: list, begin: int, end: int, k: int):
    if not end:
        end = len(array) - 1
    if not begin:
        begin = 0

    while begin < end:
        # x can be random from [begin..end]
        x = array[(end + begin) // 2]
        first_equal_x = begin
        first_greater_x = begin

        for i in range(begin, end + 1):
            cur_element = array[i]

            if cur_element == x:
                # swap current element and first greater than x
                array[i] = array[first_greater_x]
                array[first_greater_x] = cur_element
                first_greater_x += 1
            elif cur_element < x:
                # move current element to the position before first equal x
                array[i] = array[first_greater_x]
                array[first_greater_x] = array[first_equal_x]
                array[first_equal_x] = cur_element
                first_greater_x += 1
                first_equal_x += 1

        if k < first_equal_x:
            end = first_equal_x - 1
        elif k >= first_greater_x:
            begin = first_greater_x
        else:
            return


def main():
    array = list(map(int, input().split()))
    if len(array) == 3:
        return array

    # --- O(nlogn) ---
    # array.sort()

    # --- O(n) ---
    # rearrange the whole array in order to place the max element at the end
    nth_element(array=array, begin=0, end=len(array) - 1, k=len(array) - 1)
    # then rearrange array[0..-1] and place the two biggest elements at the end of array[0..-1]
    nth_element(array=array, begin=0, end=len(array) - 2, k=len(array) - 2)
    # finally rearrange array[0..-3] and place the two min elements at the beginning
    nth_element(array=array, begin=0, end=len(array) - 4, k=2)

    one, two = array[0:2]
    three, four = array[-3:-1]

    # equals -1 or 1
    max_number_sign = (array[-1] > 0) - (array[-1] < 0)

    if one * two * max_number_sign > three * four * max_number_sign:
        return one, two, array[-1]
    else:
        return three, four, array[-1]
```

## I

Вам необходимо построить поле для игры "Сапер" по его конфигурации – размерам и координатам расставленных на нем
мин.<br>
Вкратце напомним правила построения поля для игры "Сапер":

* Поле состоит из клеток с минами и пустых клеток
* Клетки с миной обозначаются символом *
* Пустые клетки содержат число k<sub>i,j</sub>, 0 ≤ k<sub>i</sub>, j ≤ 8 – количество мин на соседних клетках. Соседними
  клетками являются восемь клеток, имеющих смежный угол или сторону.

### Формат ввода

В первой строке содержатся три числа: N, 1 ≤ N ≤ 100 - количество строк на поле, M, 1 ≤ M ≤ 100 - количество столбцов на
поле, K, 0 ≤ K ≤ N ⋅ M - количество мин на поле.

В следующих K строках содержатся по два числа с координатами мин: p, 1 ≤ p ≤ N - номер строки мины, q, 1 ≤ 1 ≤ M - номер
столбца мины.

### Формат вывода

Выведите построенное поле, разделяя строки поля переводом строки, а столбцы - пробелом.

<i>Example :</i>

|         In          |        Out        |
|:-------------------:|:-----------------:|
| 3 2 2<br>1 1<br>2 2 | * 2<br>2 *<br>1 1 |

<i>Example :</i>

|  In   |    Out     |
|:-----:|:----------:|
| 2 2 0 | 0 0<br>0 0 |

<i>Example :</i>

|                In                 |                   Out                    |
|:---------------------------------:|:----------------------------------------:|
| 4 4 4<br>1 3<br>2 1<br>4 2<br>4 4 | 1 2 * 1<br>* 2 1 1<br>2 2 2 1<br>1 * 2 * |

```python
def print_field(field, n, m):
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(field[i][j], end=' ')
        print()


n, m, k = list(map(int, input().split()))

mine_coordinates = list()

for _ in range(k):
    mine_coordinates.append(tuple(map(int, input().split())))

field = list()
for i in range(n + 2):
    field.append([0] * (m + 2))

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

for mine_i, mine_j in mine_coordinates:
    for q in range(8):
        field[mine_i + di[q]][mine_j + dj[q]] += 1
for mine in mine_coordinates:
    a, b = mine[0], mine[1]
    field[a][b] = '*'

print_field(field, n, m)
```

## J

С детства Максим был неплохим музыкантом и мастером на все руки. Недавно он самостоятельно сделал несложный
перкуссионный музыкальный инструмент — треугольник. Ему нужно узнать, какова частота звука, издаваемого его
инструментом.

У Максима есть профессиональный музыкальный тюнер, с помощью которого можно проигрывать ноту с заданной частотой. Максим
действует следующим образом: он включает на тюнере ноты с разными частотами и для каждой ноты на слух определяет, ближе
или дальше она к издаваемому треугольником звуку, чем предыдущая нота. Поскольку слух у Максима абсолютный, он
определяет это всегда абсолютно верно.

Вам Максим показал запись, в которой приведена последовательность частот, выставляемых им на тюнере, и про каждую ноту,
начиная со второй, записано — ближе или дальше она к звуку треугольника, чем предыдущая нота. Заранее известно, что
частота звучания треугольника Максима составляет не менее 30 герц и не более 4000 герц.

Требуется написать программу, которая определяет, в каком интервале может находиться частота звучания треугольника.

### Формат ввода

Первая строка входного файла содержит целое число n — количество нот, которые воспроизводил Максим с помощью тюнера (2 ≤
n ≤ 1000). Последующие n строк содержат записи Максима, причём каждая строка содержит две компоненты: вещественное число
f<sub>i</sub> — частоту, выставленную на тюнере, в герцах (30 ≤ f<sub>i</sub> ≤ 4000), и слово «closer» или слово
«further» для каждой частоты, кроме первой.

Слово «closer» означает, что частота данной ноты ближе к частоте звучания треугольника, чем частота предыдущей ноты, что
формально описывается соотношением: |f<sub>i</sub> − f<sub>triangle</sub>| < |f<sub>i − 1</sub> − f<sub>triangle</sub>|
.

Слово «further» означает, что частота данной ноты дальше, чем предыдущая.

Если оказалось, что очередная нота так же близка к звуку треугольника, как и предыдущая нота, то Максим мог записать
любое из двух указанных выше слов.

Гарантируется, что результаты, полученные Максимом, непротиворечивы.

### Формат вывода

В выходной файл необходимо вывести через пробел два вещественных числа — наименьшее и наибольшее возможное значение
частоты звучания треугольника, изготовленного Максимом. Числа должны быть выведены с точностью не хуже 10<sup>−6</sup>.

<i>Example :</i>

| In                                    | Out        |
|:--------------------------------------|:-----------|
| 3<br>440<br>220 closer<br>300 further | 30.0 260.0 |

<i>Example :</i>

| In                                                  | Out         |
|:----------------------------------------------------|:------------|
| 4<br>554<br>880 further<br>440 closer<br>622 closer | 531.0 660.0 |

```python
def main():
    number_of_measures = int(input())

    borders = [30.0, 4000.0]

    last = float(input())
    for i in range(number_of_measures - 1):
        measure, estimation = input().split()
        measure = float(measure)

        # python real numbers precision patch 
        if abs(measure - last) < 1e-6:
            continue

        match estimation:
            # commented lines don't pass some tests because input can go out of range [left..right]
            # e.g. borders are [30..50], last measure was 60 and input says '45 closer'
            # in this case last - (last - measure) / 2 = 60 - (60 - 45) / 2 = 52.5 which is beyond the right border
            # thus min and max functions are used
            case 'closer':
                if last > measure:
                    # borders[1] = last - ((last - measure) / 2)
                    borders[1] = min(borders[1], last - ((last - measure) / 2))
                else:
                    # borders[0] = last + ((measure - last) / 2)
                    borders[0] = max(borders[0], last + ((measure - last) / 2))
            case 'further':
                if last > measure:
                    # borders[0] = measure + ((last - measure) / 2)
                    borders[0] = max(borders[0], measure + ((last - measure) / 2))
                else:
                    # borders[1] = measure - ((measure - last) / 2)
                    borders[1] = min(borders[1], measure - ((measure - last) / 2))
        last = measure
    print(*borders)
```