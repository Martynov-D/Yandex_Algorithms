import queue


def main():
    with open('input.txt', 'r') as inf:
        number_of_buildings, number_of_maps = map(int, inf.readline().split())

        # Элемент графа - здание.
        # Массив соседей - здания, к которым ведут дороги.
        # Каждый сосед подписан номером карты, на которой находится ведущая в него дорога.
        graph = [[] for _ in range(number_of_buildings + 1)]
        for i in range(number_of_maps):
            number_of_roads = int(inf.readline().strip())
            for _ in range(number_of_roads):
                road = tuple(map(int, inf.readline().split()))
                graph[road[0]].append((road[1], i))
                graph[road[1]].append((road[0], i))

    # Расстояния - количество загрузок карт
    distances = [-1 for _ in range(number_of_buildings + 1)]
    parents = [set() for _ in range(number_of_buildings + 1)]
    q = queue.Queue()
    distances[1] = 1
    # Все переходы из начальной точки
    for neighbour in graph[1]:
        q.put(neighbour)
        distances[neighbour[0]] = 1
        parents[neighbour[0]].add(neighbour[1])

    while not q.empty():
        position, map_number = q.get()
        temp = distances[position]
        for neighbour in graph[position]:
            distance = temp
            if map_number != neighbour[1]:
                distance += 1

            if (distances[neighbour[0]] == -1) or (distances[neighbour[0]] > distance):
                q.put(neighbour)
                parents[neighbour[0]].add(neighbour[1])

                distances[neighbour[0]] = distance
            
            if (distances[neighbour[0]] == distance) and (neighbour[1] not in parents[neighbour[0]]):
                q.put(neighbour)
                parents[neighbour[0]].add(neighbour[1])
                    
    print(distances[-1])

if __name__ == '__main__':
    main()

# TODO Time Limit
