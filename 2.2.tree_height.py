# решение через список родителей (снизу-вверх)
def get_height(in1, in2):

    # получаем количество вершин и список родителей
    n = int(in1)
    parents = list(map(int, in2.split(" ")))

    # задаем словарь для хранения расстояний от вершины до корня (уровни дерева)
    levels = {}

    # идем вверх по дереву и считаем уровень вершины
    def up(v):
        parent = parents[v]
        if parent == -1:
            return 1
        if v not in levels:
            levels[v] = up(parent) + 1
        return levels[v]

    # находим максимальный уровень вершин, пройдя по всем вершинам
    max_level = 0
    for v in range(n):
        max_level = max(max_level, up(v))

    return max_level


# решение через список детей (сверху-вниз)
def get_height_2(in1, in2):
    from collections import deque

    # получаем количество вершин и список родителей
    n = int(in1)
    parents = list(map(int, in2.split(" ")))

    # по списку родителей строим список детей и получаем номер корня
    graph = [[] for _ in range(n)]
    num_root = -1
    for i, v in enumerate(parents):
        if v != -1:
            graph[v].append(i)
        else:
            num_root = i

    # используем стек
    q = deque()
    # кладем корень в стек
    q.append((num_root, 1))
    max_height = 1

    # пока очередь не пустая
    while q:
        # извлекаем первый элемент очереди
        head = q.popleft()

        # если есть дочерние элементы
        if graph[head[0]]:
            height = head[1] + 1

            # проходим по всем дочерним элементам и помещаем их очередь, параллельно увеличивая индекс высоты
            for child in graph[head[0]]:
               q.append((child, height))
            max_height = max(max_height, height)

    return max_height


def main():
    # получаем высоту дерева
    print(get_height(input(), input()))


def test():
    assert get_height("10", "9 7 5 5 2 9 9 9 2 -1") == 4


if __name__ == "__main__":
    main()
