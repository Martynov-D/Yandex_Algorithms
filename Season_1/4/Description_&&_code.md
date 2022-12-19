Link: <https://contest.yandex.ru/contest/27665/enter/>

## A

Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре
различны. Для одного данного слова определите его синоним.

### Формат ввода

Программа получает на вход количество пар синонимов N. Далее следует N строк, каждая строка содержит ровно два
слова-синонима. После этого следует одно слово.

### Формат вывода

Программа должна вывести синоним к данному слову. Примечание

Эту задачу можно решить и без словарей (сохранив все входные данные в списке), но решение со словарем будет более
простым.

<i>Example 1:</i>

| In                                                    | Out |
|-------------------------------------------------------|-----|
| 3<br>Hello Hi<br>Bye Goodbye<br>List Array<br>Goodbye | Bye |

<i>Example 2:</i>

| In                   | Out  |
|----------------------|------|
| 1<br>beep Car<br>Car | beep |

<i>Example 3:</i>

| In                                                | Out        |
|---------------------------------------------------|------------|
| 2<br>Ololo Ololo<br>Numbers 1234567890<br>Numbers | 1234567890 |

```python
def main():
    number_of_pairs = int(input())
    word_pairs = dict()

    for _ in range(number_of_pairs):
        key, value = input().split()
        word_pairs[key] = value
        word_pairs[value] = key

    print(word_pairs[input()])
```

## B

Во входном файле (вы можете читать данные из файла input.txt) записан текст. Словом считается последовательность
непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки. Для
каждого слова из этого текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.

<i>Example 1:</i>

| In                    | Out       |
|-----------------------|-----------|
| one two one tho three | 0 0 1 0 0 |

<i>Example 2:</i>

| In                                                                                                                                                                                             | Out                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| She sells sea shells on the sea shore;<br>The shells that she sells are sea shells I'm sure.<br>So if she sells sea shells on the sea shore,<br>I'm sure that the shells are sea shore shells. | 0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0 |

<i>Example 3:</i>

| In               | Out     |
|------------------|---------|
| aba aba; aba @?" | 0 0 1 0 |

```python
def main():
    text = list()
    with open('input.txt', 'r') as f:
        for line in f:
            text.extend(line.split())

    words = dict()

    for word in text:
        if word not in words:
            words[word] = 0
        print(words[word], end=' ')
        words[word] += 1
```

## C

Дан текст. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое
меньше в лексикографическом порядке.

<i>Example 1:</i>

| In                                | Out    |
|-----------------------------------|--------|
| apple orange banana banana orange | banana |

<i>Example 2:</i>

| In                                            | Out  |
|-----------------------------------------------|------|
| oh you touch my tralala mmm my ding ding dong | ding |

<i>Example 3:</i>

| In                                                        | Out |
|-----------------------------------------------------------|-----|
| q w e r t y u i o p<br>a s d f g h j k l<br>z x c v b n m | a   |

```python
def main():
    text = list()
    with open('input.txt', 'r') as f:
        for l in f:
            text.extend(l.split())

    words = dict()

    for word in text:
        if word not in words:
            words[word] = 0
        words[word] += 1

    words = {k: words[k] for k in sorted(words)}

    print(list(words.keys())[list(words.values()).index(max(words.values()))])
```

## D

На региональном этапе Всероссийской олимпиады школьников по информатике в 2009 году предлагалась следующая задача.

Всем известно, что со временем клавиатура изнашивается,и клавиши на ней начинают залипать. Конечно, некоторое время
такую клавиатуру еще можно использовать, но для нажатий клавиш приходиться использовать большую силу.

При изготовлении клавиатуры изначально для каждой клавиши задается количество нажатий,которое она должна выдерживать.
Если знать эти величины для используемой клавиатуры,то для определенной последовательности нажатых клавиш можно
определить,какие клавиши в процессе их использования сломаются, а какие — нет.

Требуется написать программу, определяющую, какие клавиши сломаются в процессе заданного варианта эксплуатации
клавиатуры.

### Формат ввода

Первая строка входных данных содержит целое число n (1 ≤ n ≤ 1000) —количество клавиш на клавиатуре. Вторая строка
содержит n целых чисел —с1, с2, … , сn, где сi (1 ≤ ci ≤ 100000) — количество нажатий,выдерживаемых i-ой клавишей.
Третья строка содержит целое число k (1 ≤ k ≤ 100000) — общее количество нажатий клавиш, и последняя строка содержит k
целых чисел pj (1 ≤ pj ≤ n) — последовательность нажатых клавиш.

### Формат вывода

Программа должна вывести n строк, содержащих информацию об исправности клавиш.Если i-я клавиша сломалась, то i-ая строка
должна содержать слово YES,если же клавиша работоспособна — слово NO.

<i>Example 1:</i>

| In                                                       | Out                          |
|----------------------------------------------------------|------------------------------|
| 5<br>1 50 3 4 3<br>16<br>1 2 3 4 5 1 3 3 4 5 5 5 5 5 4 5 | YES<br>NO<br>NO<br>NO<br>YES |

```python
def main():
    keys = dict()
    i = 1
    number_of_keys = int(input())
    for v in map(int, input().split()):
        keys[i] = v
        i += 1

    number_of_pushes = int(input())
    for i in list(map(int, input().split())):
        keys[i] -= 1

    for key in keys.values():
        if key < 0:
            print('YES')
        else:
            print('NO')
```

## E

Для строительства двумерной пирамиды используются прямоугольные блоки, каждый из которых характеризуется шириной и
высотой. Можно поставить один блок на другой, только если ширина верхнего блока строго меньше ширины нижнего (блоки
нельзя поворачивать). Самым нижним в пирамиде может быть блок любой ширины. По заданному набору блоков определите,
пирамиду какой наибольшей высоты можно построить из них.

### Формат ввода

В первой строке входных данных задается число N — количество блоков (
1 ≤ N ≤ 1 0 0 0 0 0
). В следующих N строках задаются пары натуральных чисел w i и h i
(
1 ≤ w i , h i ≤ 1 0 9
) — ширина и высота блока соответственно.

### Формат вывода

Выведите одно целое число — максимальную высоту пирамиды.

<i>Example 1:</i>

| In                      | Out |
|-------------------------|-----|
| 3<br>3 1<br>2 2<br>3 3  | 5   |

```python
def main():
    number_of_blocks = int(input())

    blocks = dict()

    for _ in range(number_of_blocks):
        block = tuple(map(int, input().split()))
        if block[0] in blocks:
            blocks[block[0]] = max(blocks[block[0]], block[1])
        else:
            blocks[block[0]] = block[1]

    result_height = 0
    for width, height in blocks.items():
        result_height += height

    print(result_height)
```

## F

Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись вида
Покупатель товар количество, где Покупатель — имя покупателя (строка без пробелов), товар — название товара (строка без
пробелов), количество — количество приобретенных единиц товара. Создайте список всех покупателей, а для каждого
покупателя подсчитайте количество приобретенных им единиц каждого вида товаров.

### Формат ввода

Вводятся сведения о покупках в указанном формате.

### Формат вывода

Выведите список всех покупателей в лексикографическом порядке, после имени каждого покупателя выведите двоеточие, затем
выведите список названий всех приобретенных данным покупателем товаров в лексикографическом порядке, после названия
каждого товара выведите количество единиц товара, приобретенных данным покупателем. Информация о каждом товаре выводится
в отдельной строке.

<i>Example 1:</i>

| In                                                                                                               | Out                                                                               |
|------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Ivanov paper 10<br>Petrov pens 5<br>Ivanov marker 3<br>Ivanov paper 7<br>Petrov envelope 20<br>Ivanov envelope 5 | Ivanov:<br>envelope 5<br>marker 3<br>paper 17<br>Petrov:<br>envelope 20<br>pens 5 |

<i>Example 2:</i>

| In                                                                                                                                                                                                                      | Out                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Ivanov aaa 1<br>Petrov aaa 2<br>Sidorov aaa 3<br>Ivanov aaa 6<br>Petrov aaa 7<br>Sidorov aaa 8<br>Ivanov bbb 3<br>Petrov bbb 7<br>Sidorov aaa 345<br>Ivanov ccc 45<br>Petrov ddd 34<br>Ziborov eee 234<br>Ivanov aaa 45 | Ivanov:<br>aaa 52<br>bbb 3<br>ccc 45<br>Petrov:<br>aaa 9<br>bbb 7<br>ddd 34<br>Sidorov:<br>aaa 356<br>Ziborov:<br>eee 234 |

```python
def main():
    people = dict()
    with open('input.txt', 'r') as f:
        for line in f:
            name, good, amount = line.split()
            if name not in people:
                people[name] = dict()
            if good not in people[name]:
                people[name][good] = 0
            people[name][good] += int(amount)

    for name in sorted(people.keys()):
        print(f'{name}:')
        for good in sorted(people[name].keys()):
            print(f'{good} {people[name][good]}')
```

## G

Некоторый банк хочет внедрить систему управления счетами клиентов, поддерживающую следующие операции:

Пополнение счета клиента. Снятие денег со счета. Запрос остатка средств на счете. Перевод денег между счетами клиентов.
Начисление процентов всем клиентам.

Вам необходимо реализовать такую систему. Клиенты банка идентифицируются именами (уникальная строка, не содержащая
пробелов). Первоначально у банка нет ни одного клиента. Как только для клиента проводится операция пололнения, снятия
или перевода денег, ему заводится счет с нулевым балансом. Все дальнейшие операции проводятся только с этим счетом.
Сумма на счету может быть как положительной, так и отрицательной, при этом всегда является целым числом.

### Формат ввода

Входной файл содержит последовательность операций. Возможны следующие операции: DEPOSIT name sum - зачислить сумму sum
на счет клиента name. Если у клиента нет счета, то счет создается. WITHDRAW name sum - снять сумму sum со счета клиента
name. Если у клиента нет счета, то счет создается. BALANCE name - узнать остаток средств на счету клиента name. TRANSFER
name1 name2 sum - перевести сумму sum со счета клиента name1 на счет клиента name2. Если у какого-либо клиента нет
счета, то ему создается счет. INCOME p - начислить всем клиентам, у которых открыты счета, p% от суммы счета. Проценты
начисляются только клиентам с положительным остатком на счету, если у клиента остаток отрицательный, то его счет не
меняется. После начисления процентов сумма на счету остается целой, то есть начисляется только целое число денежных
единиц. Дробная часть начисленных процентов отбрасывается.

### Формат вывода

Для каждого запроса BALANCE программа должна вывести остаток на счету данного клиента. Если же у клиента с запрашиваемым
именем не открыт счет в банке, выведите ERROR.

<i>Example 1:</i>

| In                                                                                                                                        | Out                 |
|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------|
| DEPOSIT Ivanov 100<br>INCOME 5<br>BALANCE Ivanov<br>TRANSFER Ivanov Petrov 50<br>WITHDRAW Petrov 100<br>BALANCE Petrov<br>BALANCE Sidorov | 105<br>-50<br>ERROR |

<i>Example 2:</i>

| In                                                                                                                                                                                                                                             | Out                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| BALANCE a<br>BALANCE b<br>DEPOSIT a 100<br>BALANCE a<br>BALANCE b<br>WITHDRAW a 20<br>BALANCE a<br>BALANCE b<br>WITHDRAW b 78<br>BALANCE a<br>BALANCE b<br>WITHDRAW a 784<br>BALANCE a<br>BALANCE b<br>DEPOSIT b 849<br>BALANCE a<br>BALANCE b | ERROR<br>ERROR<br>100<br>ERROR<br>80<br>ERROR<br>80<br>-78<br>-704<br>-78<br>-704<br>771 |

```python
def main():
    def check_customer(name):
        if name not in customers:
            customers[name] = 0

    def balance(name):
        if name not in customers:
            return 'ERROR'
        return customers[name]

    def deposit(name, amount):
        check_customer(name)
        customers[name] += amount

    def withdraw(name, amount):
        check_customer(name)
        customers[name] -= amount

    def transfer(name1, name2, amount):
        check_customer(name1)
        check_customer(name2)
        customers[name1] -= amount
        customers[name2] += amount

    def income(amount):
        for name in customers.keys():
            if customers[name] > 0:
                customers[name] += int(customers[name] * (amount / 100))

    customers = dict()

    with open('input.txt', 'r') as f:
        for line in f:
            operation = line.split()
            match operation[0]:
                case 'DEPOSIT':
                    deposit(operation[1], int(operation[2]))
                case 'WITHDRAW':
                    withdraw(operation[1], int(operation[2]))
                case 'TRANSFER':
                    transfer(operation[1], operation[2], int(operation[3]))
                case 'INCOME':
                    income(int(operation[1]))
                case 'BALANCE':
                    print(balance(operation[1]))
```

## H

Расшифровка письменности Майя оказалась более сложной задачей, чем предполагалось ранними исследованиями. На протяжении
более чем двух сотен лет удалось узнать не так уж много. Основные результаты были получены за последние 30 лет.

Письменность Майя основывается на маленьких рисунках, известных как значки, которые обозначают звуки. Слова языка Майя
обычно записываются с помощью этих значков, которые располагаются рядом друг с другом в некотором порядке.

Одна из проблем расшифровки письменности Майя заключается в определении этого порядка. Рисуя значки некоторого слова,
писатели Майя иногда выбирали позиции для значков, исходя скорее из эстетических взглядов, а не определенных правил. Это
привело к тому, что, хотя звуки для многих значков известны, археологи не всегда уверены, как должно произноситься
записанное слово.

Археологи ищут некоторое слово W. Они знают значки для него, но не знают все возможные способы их расположения.
Поскольку они знают, что Вы приедете на IOI ’06, они просят Вас о помощи. Они дадут Вам g значков, составляющих слово W,
и последовательность S всех значков в надписи, которую они изучают, в порядке их появления. Помогите им, подсчитав
количество возможных появлений слова W.

Задание Напишите программу, которая по значкам слова W и по последовательности S значков надписи подсчитывает количество
всех возможных вхождений слова W в S, то есть количество всех различных позиций идущих подряд g значков в
последовательности S, которые являются какой-либо перестановкой значков слова W .

### Формат ввода

1 ≤ g ≤ 3 000, g – количество значков в слове W

g ≤ |S| ≤ 3 000 000 где |S| – количество значков в последовательности S

На вход программы поступают данные в следующем формате:

СТРОКА 1: Содержит два числа, разделенных пробелом – g и |S|. СТРОКА 2: Содержит g последовательных символов, с помощью
которых записывается слово W . Допустимы символы: ‘a’-‘z’ и ‘A’-‘Z’; большие и маленькие буквы считаются различными.
СТРОКА 3: Содержит |S| последовательных символов, которые представляют значки в надписи. Допустимы символы: ‘a’-‘z’ и
‘A’-‘Z’; большие и маленькие буквы считаются различными.

### Формат вывода

Единственная строка выходных данных программы должна содержать количество возможных вхождений слова W в S.

<i>Example :</i>

| In                          | Out |
|-----------------------------|-----|
| 4 11<br>cAda<br>AbrAcadAbRa | 2   |

Работает на Python 3.7 PyPy 7.3.3. На Python 3.10 и C++17 GNU уходит за ограничение по времени.

```python
def make_dict(s):
    d = dict()
    for char in s:
        if char not in d:
            d[char] = 0
        d[char] += 1

    return d


def match_dicts(d1, d2):
    matches = 0
    for key in d1:
        if key in d2 and d1[key] == d2[key]:
            matches += 1
    return matches


def modify_dict(buffer_dict, word_dict, letter, modifier):
    count = 0
    if letter not in buffer_dict:
        buffer_dict[letter] = 0

    if letter in word_dict and word_dict[letter] == buffer_dict[letter]:
        count = -1
    buffer_dict[letter] += modifier
    if letter in word_dict and word_dict[letter] == buffer_dict[letter]:
        count = 1
    return count


def main():
    word_length, string_length = map(int, input().split())

    word = input()
    string = input()

    word_dict = make_dict(word)
    buffer_dict = make_dict(string[0:word_length])

    matching_letters = match_dicts(word_dict, buffer_dict)
    occurrences = 0
    if matching_letters == len(word_dict):
        occurrences += 1

    for i in range(word_length, string_length):
        matching_letters += modify_dict(buffer_dict, word_dict, string[i - word_length], -1)
        matching_letters += modify_dict(buffer_dict, word_dict, string[i], 1)

        if matching_letters == len(word_dict):
            occurrences += 1

    print(occurrences)
```

```C++
#include <fstream>
#include <map>


void insertIntoDict(std::map<char, int> &a, const char letter)
{
	if (a.find(letter) == a.end())
		a.insert(std::make_pair(letter, 0));
	++a.at(letter);
}


void deleteFromDict(std::map<char, int> &a, const char letter)
{
	if (a.find(letter)->second == 1)
		a.erase(letter);
	else
		--a.at(letter);
}


std::map<char, int> makeDict(const std::string &line)
{
	std::map<char, int> stringDictionary{};
	for (const char letter : line)
	{
		insertIntoDict(stringDictionary, letter);
	}
	return stringDictionary;
}


int dictionaryMatching(const std::map<char, int>& a, const std::map<char, int>& b)
{
	int numberOfMatchingLetters{ 0 };
	std::map<char, int>::const_iterator symbol{ a.cbegin() };
	while (symbol != a.cend())
	{
		if (b.find(symbol->first) != b.cend() && b.at(symbol->first) == symbol->second)
			++numberOfMatchingLetters;
		++symbol;
	}
	return numberOfMatchingLetters;
}


int main()
{
	std::ifstream inf{ "input.txt" };
	std::ofstream outf("output.txt");

	int wLength{};
	int sLength{};
	inf >> wLength;
	inf >> sLength;

	std::string word{};
	std::string line{};
	inf >> word;
	inf >> line;

	std::map<char, int> wordDictionary{ makeDict(word) };
	std::map<char, int> lineDictionary{ makeDict(line.substr(0, wLength)) };

	std::size_t wordDictionarySize = wordDictionary.size();
	int numberOfMatchingLetters{ dictionaryMatching(wordDictionary, lineDictionary) };
	int occurrencies{ 0 };
	if (numberOfMatchingLetters == wordDictionarySize)
		++occurrencies;

	for (int i{ wLength }; i < line.size(); ++i)
	{
		char symbolToInsert{ line[i] };
		char symbolToDelete{ line[i - wLength] };

		if (symbolToInsert == symbolToDelete)
		{
			if (numberOfMatchingLetters == wordDictionarySize)
				++occurrencies;
			continue;
		}

		insertIntoDict(lineDictionary, symbolToInsert);
		deleteFromDict(lineDictionary, symbolToDelete);
		numberOfMatchingLetters = dictionaryMatching(lineDictionary, wordDictionary);
		if (numberOfMatchingLetters == wordDictionarySize)
			++occurrencies;
	}

	outf << occurrencies;

	return 0;
}
```

## I

Учительница задала Пете домашнее задание — в заданном тексте расставить ударения в словах, после чего поручила Васе
проверить это домашнее задание. Вася очень плохо знаком с данной темой, поэтому он нашел словарь, в котором указано, как
ставятся ударения в словах. К сожалению, в этом словаре присутствуют не все слова. Вася решил, что в словах, которых нет
в словаре, он будет считать, что Петя поставил ударения правильно, если в этом слове Петей поставлено ровно одно
ударение. Оказалось, что в некоторых словах ударение может быть поставлено больше, чем одним способом. Вася решил, что в
этом случае если то, как Петя поставил ударение, соответствует одному из приведенных в словаре вариантов, он будет
засчитывать это как правильную расстановку ударения, а если не соответствует, то как ошибку. Вам дан словарь, которым
пользовался Вася и домашнее задание, сданное Петей. Ваша задача — определить количество ошибок, которое в этом задании
насчитает Вася.

### Формат ввода

Вводится сначала число N — количество слов в словаре (0≤N≤20000). Далее идет N строк со словами из словаря. Каждое слово
состоит не более чем из 30 символов. Все слова состоят из маленьких и заглавных латинских букв. В каждом слове заглавная
ровно одна буква — та, на которую попадает ударение. Слова в словаре расположены в алфавитном порядке. Если есть
несколько возможностей расстановки ударения в одном и том же слове, то эти варианты в словаре идут в произвольном
порядке. Далее идет упражнение, выполненное Петей. Упражнение представляет собой строку текста, суммарным объемом не
более 300000 символов. Строка состоит из слов, которые разделяются между собой ровно одним пробелом. Длина каждого слова
не превышает 30 символов. Все слова состоят из маленьких и заглавных латинских букв (заглавными обозначены те буквы, над
которыми Петя поставил ударение). Петя мог по ошибке в каком-то слове поставить более одного ударения или не поставить
ударения вовсе.

### Формат вывода

Выведите количество ошибок в Петином тексте, которые найдет Вася.

<i>Example 1:</i>

| In                                                                 | Out |
|--------------------------------------------------------------------|-----|
| 4<br>cAnnot<br>cannOt<br>fOund<br>pAge<br>thE pAge cAnnot be found | 2   |

<i>Example 2:</i>

| In                                                                 | Out |
|--------------------------------------------------------------------|-----|
| 4<br>cAnnot<br>cannOt<br>fOund<br>pAge<br>The PAGE cannot be found | 4   |

<i>Example 3:</i>

| In                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Out |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| 0<br>ciFqrfIxe LgvqquN zvdlhnXJ tizFPXtv JxqWqgnR CabaJ hFYoqbhH UyfiTXO YvAylvnc ymtHHfnqh bmTLsEnh hikroekt dtVSftFBz ofQrMfo jGTGofv dVRwfJw UaRfzE wbjjGsM xKcezhleq XskqyXtl pWCkyr JcuiiawHw hHBbOV pIfztqkuo PNbjXhtoi lvthZdUc oozdiZCq xDdnpRqsD HDfocjpl aziTbCh jsJMkTpaG voKfnjYb ADtpndbo gwOkCvJs hGnvtbM NkFodqOwy BOgxWv qzMsbelpO tlQnic QlxjhTzNj OZvzmoNX NlbLsjq OvkpysLzc BFCjEESh aiLyKJas zhJbcdu vqxrKhgke BsEikapC aCCoHAFR qNSYNouc TboUQd bOJWCAy NiNkHPmA wsGXhub xIvDhv qeGgpTBkd XPOkfsxz bbgcyuWq YHioAxh mngcZbpgh qgbfVztk JMusos ogpskgdN HUmedvmA GhhpYKH vduijcpv rfMZlB rvpodvq UogggJX yhnKvOpz cKQHazal xdXpPMCzn zaYdrbic FYDsrfaF kFpUcXtY jihQVZ nhpgJXoT rwJokNFH eGvoNulk LugdwQRbl xlRQdy mOrvmCmhG tJpEDolo zLhXCegyl Orrnefa sQqsjckkm BaadhPSXa vLmbthY mlwXEbpns oLctMjmM spQHUtA qnxUrLGo ScAndtRh apdwiTV odtrlufr zkrreoWHT wbOJLyIvn TDPtdjFp CJtnhbNr ohkLVpww vJLdOfp ctswuolD kuIdtiWLq pHQvvlN uzEgrQhpG ncHyqZzt gkntqtmx ZAvUjYgJ hbjSXnN URnTcdbRk wMdRlrQ ilpvgMpja oIjXxmG sdnIJTkk bFvhViK dpdtgpt CembyhyMM RcBIirR rWyYzJfc UNbTfQQ plxhCpee bUbkgdDF JTgQAQhvp onFayvlm rykjyldhw xAuEnxF phbhlXB xxDDxfSfM aPHXcXsag sTseOhrrY MMiaCH avfBbeIfl hrtuxe zJlubLs Wwwdjvc JBnqWcAl hDXOdeHZr Nelvhp ydmbzqym kzbCxuN rNQCDbeqB VRaax yykZbEzOc XomeWckS jBrCrHrx FzGrd YvfUzRryb YYPSRO wxBazrm EkezBXg aUiYcod aTtjEEpz WczSYbDx tlFeIKB LlSQDtyVa iMGfoQ WyXVU wakvcqSU loKOoSnzA pWywmptia RcEMjACB bfyrkwpLp iSofdn SacAoja uIkcgpWnM dkqErpG nkxTwHfh srejafR rjXxUCQ BCstjy LBdeArjn SbunWWcd FmTkfGwh nyGRjOi VlZjliwD lQhjguWx IkemfP VGfqFBuiN aYrbvKu iabtpq QnjzcKE sffhhZYY JuooLppkr LqyjiBC WySPUmsQb CXjftV TmtgreN cicNuaor YIgdgc vTFwiGktI TNFmWdHU DpfEtwtf zssykzEsf xcsCKfnaS OBEwUVkzg PgArpsz RmUcaQels JmJaqn IcXnrvhkg vgkOPzmv BezbGaMfb bnjTmLse TnkNLq CxfpAoD slhLtnoaP jnppioo STcoufpS XmRtQqd yDpbsld qrVIEXn VZhmozgvr zuELbtea WiOopcPg vRwLRoy TyJkPUvOq yZSsjoi AzlwLPf suwNmPrzF kuJeUivG EnTHwlj XpZkNZH xygjBcx bTytkWFW ygKis iwjgktgw DzFDkhb elWPfddxy TyvlSNVR OBqjNCtXI cSYxJTb DqedLuqN vxikfztEc AbcQgnxiS bdCmDnn VbLDUWsz eeuucmp osIYklu sLXmxRipG yswHjZayD bMihpnRs lmyVpf gtfkgpmbB buPjpqli yxFSIu Ggjzeqm dTqrvPtei XduXypxn BykKgHhqe ewcUDvM lxWoiXBT HeqhAZu ialinsqW lcNzJmK yCKPbQrz hOjxGWvPq HgenCiuw QnWaEtz lRvwixAj otnJuciJ qtNWZPtL tJYiHzUiG rNhaIjil Oggvgmdq nhylWth VhrHlcnJV ceHFAVnU udtpWoJ wiQAeN mUkmTUv BqnLMdeSy kiffoynx vsnzxZe QbyfijgM ecxxWebWo TFoLnXouN SldaeWjV fuXlPWzBg qNNShyw avvNUgmP lhblkew svZdutKT avlFkl Afntea NrGVToH Hlvkxnut NbNbQXnc ugqqBFWcq bphIBvYpz FuuAUB CnqFfWxy lNdVncXmk UBvozFuqz muVHqMpa vcyQgcXN lfzcMdN eMmz ehXopYXAg GjBapgXVY qimorSZZt YEyoXzclm eUlyvxi aFrOSW htxGkVuJ ydszmKyb zAvzlkXM oRQizsGBz gZodlbKg pwQSugvyq MOvfpsCs tGNJBf lZqEdtPD sHYmFjcH wkRltsoYz qkWmhhBJ wgATDnhc HnbkMwnRv oSolCjBj xyQfzgenj xBtaqrEj eoCCfSg xYgfXZ htSgaFlbt DPrfLUw bdhrUaqT IabsomJE cyVtEg SMntmDjx jwwkwJkRo HeFyGSaTh KiSTzh dBCcqt vnAunEzf kGzwbur qmkMBbGCw Tdkunrkh YrYVnrbC muJSHjn Unuwgjfj ObbZfLsWd UjmxpJN KNlbLhF jFlbrLf pyOglEK | 296 |

```python
def getWordStress(word: str):
    stresses = set()
    for i in range(len(word)):
        if word[i].isupper():
            stresses.add(i)
    return stresses


def main():
    with open('input.txt', 'r') as f:
        number = int(f.readline())
        dictionary = dict()
        for _ in range(number):
            word = f.readline().strip()
            lowercase = word.lower()
            if lowercase not in dictionary:
                dictionary[lowercase] = set()
            dictionary[lowercase].update(getWordStress(word))

        text = f.readline()

    errors = 0

    for word in text.split():
        wordStress = getWordStress(word)
        if len(wordStress) == 1:
            lowercase = word.lower()
            if lowercase in dictionary:
                if wordStress.pop() not in dictionary[lowercase]:
                    errors += 1
        else:
            errors += 1
    print(errors)
```

## J

Преподаватель курса ОиМП заказал у одного известного психолога полное психологическое обследование всех студентов,
поступивших на ФНК с целью выяснить их склонность к списыванию еще до начала занятий и отчислить их за списывание еще до
того как они приступят к занятиям и смогут позорить ФНК своими преступлениями. Психолог, привлеченный для проведения
обследования, известен своим инновационным методом, позволяющим понять склонность к списыванию студента по наиболее
часто используемому им в программах идентификатору. Помогите известному психологу определить, какие из студентов
потенциально являются преступниками. Напишите программу, которая по приведенной программе выяснит наиболее часто
используемый в ней идентификатор.

Поскольку разные студенты на тестировании пишут программы на разных языках программирования, ваша программа должна уметь
работать с произвольным языком. Поскольку в разных языках используются различные ключевые слова, то список ключевых слов
в анализируемом языке предоставляется на вход программе. Все последовательности из латинских букв, цифр и знаков
подчеркивания, которые не являются ключевыми словами и содержат хотя бы один символ, не являющийся цифрой, могут быть
идентификаторами. При этом в некоторых языках идентификаторы могут начинаться с цифры, а в некоторых - нет. Если
идентификатор не может начинаться с цифры, то последовательность, начинающаяся с цифры, идентификатором не является.
Кроме этого, задано, является ли язык чувствительным к регистру символов, используемых в идентификаторах и ключевых
словах.

### Формат ввода

В первой строке вводятся число n - количество ключевых слов в языке (0 <= n <= 50) и два слова C и D, каждое из которых
равно либо "yes", либо "no". Слово C равно "yes", если идентификаторы и ключевые слова в языке чувствительны к регистру
символов, и "no", если нет. Слово D равно "yes", если идентификаторы в языке могут начинаться с цифры, и "no", если нет.

Следующие n строк содержат по одному слову, состоящему из букв латинского алфавита и символов подчеркивания - ключевые
слова. Все ключевые слова непусты, различны, при этом, если язык не чувствителен к регистру, то различны и без учета
регистра. Длина каждого ключевого слова не превышает 50 символов.

Далее до конца входных данных идет текст программы. Он содержит только символы с ASCII-кодами от 32 до 126 и переводы
строки.

Размер входных данных не превышает 10 килобайт. В программе есть хотя бы один идентификатор.

### Формат вывода

Выведите идентификатор, встречающийся в программе максимальное число раз. Если таких идентификаторов несколько, следует
вывести тот, который встречается в первый раз раньше. Если язык во входных данных не чувствителен к регистру, то можно
выводить идентификатор в любом регистре.

<i>Example 1:</i>

<table>
<tr>
<td> <b>In</b> </td> <td> <b>Out</b> </td>
</tr>
<tr>
<td>
0 yes no

```C++
int main() {
  int a;
  int b;
  scanf("%d%d", &a, &b);
  printf("%d", a + b);
}
```

</td><td>int</td>
</tr>
</table>

<i>Example 2:</i>

<table>
<tr>
<td> <b>In</b> </td> <td> <b>Out</b> </td>
</tr>
<tr>
<td>
0 yes no

```C++
#define INT int
int main() {
  INT a, b;
  scanf("%d%d", &a, &b);
  printf("%d %d", a + b, 0);
}
```

</td><td>d</td>
</tr>
</table>

<i>Example 3:</i>

<table>
<tr>
<td> <b>In</b> </td> <td> <b>Out</b> </td>
</tr>
<tr>
<td>
6 no no

```Pascal
program
var
begin
end
while
for
program sum;
var
  A, B: integer;
begin
  read(A, b);
  writeln(a + b);
end.
```

</td><td>a</td>
</tr>
</table>

<i>Example 4:</i>

<table>
<tr>
<td> <b>In</b> </td> <td> <b>Out</b> </td>
</tr>
<tr>
<td>
1 yes yes

```
_
a = 0h
b = 0h
c = 0h
```

</td>
<td>0h</td>
</tr>
</table>

```python
def removeSymbols(line: str):
    result = list()
    for c in line:
        if c.isalpha() or c.isdigit() or c == '_':
            result.append(c)
        else:
            result.append(' ')
    return ''.join(result)


def checkWord(word: str, can_start_with_digit: bool):
    if not word.isdigit() and (can_start_with_digit or not word[0].isdigit()):
        return True
    return False


with open('input.txt', 'r') as f:
    number_of_key_words, sensitive_to_register, can_start_with_digit = f.readline().split()
    number_of_key_words = int(number_of_key_words)
    sensitive_to_register = sensitive_to_register == 'yes'
    can_start_with_digit = can_start_with_digit == 'yes'

    key_words = set()
    for _ in range(number_of_key_words):
        word = f.readline().strip()
        if not sensitive_to_register:
            word = word.lower()
        key_words.add(word)

    words_counter = dict()
    wordPosition = 0

    for line in f.readlines():
        line = removeSymbols(line.strip())
        for word in line.split():
            if not sensitive_to_register:
                word = word.lower()
            if word not in key_words:
                if checkWord(word, can_start_with_digit):
                    wordPosition += 1
                    if word not in words_counter:
                        words_counter[word] = [0, wordPosition]
                    words_counter[word][0] += 1

answer = ''
best_word = [0, 0]

for word, counter in words_counter.items():
    if counter[0] > best_word[0] or (counter[0] == best_word[0] and counter[1] < best_word[1]):
        best_word = counter
        answer = word

print(answer)
```