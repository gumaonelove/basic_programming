from openpyexcel import load_workbook


def __read_file():
    '''
    Читаем файл excel
    :return: содержимое листа
    '''
    wb = load_workbook(filename='map.xlsx', read_only=True)
    ws = wb['Sheet1']
    return ws


def get_graph():
    '''
    :return: возвращаем неориентированный взвешенный граф
    '''
    ws = __read_file()

    inf = float('Inf')
    _len = 0
    for row in ws.rows: _len += 1

    G = [[inf] * _len for _ in range(_len)]

    i, j = 0, 0
    for row in ws.rows:
        for cell in row:
            if cell.value:
                G[i][j] = cell.value
                G[j][i] = cell.value
            j += 1
        i += 1
        j = 0
    return G


def get_list_address():
    '''
    :return: Список возможных адресов
    '''
    ws = __read_file()
    _list = []
    for row in ws.rows:
        for address in row:
            if address.value:
                _list.append(address.value)
        break
    return _list


def __dijkstra(G, s):
    '''
    Алгоритм Дейкстреры
    :param G: Взвешенный граф заданный матрицей смежности
    :param s: Вершина старта
    :return: Массив кротчайших расстояний от старта до указанной вершины
    '''

    n = len(G) # колво вершин графа
    Q = [(0, s)] # очередь
    inf = float('Inf') # бесконечность
    d = [inf for _ in range(n)] # массив кратчайших расстояний
    d[s] = 0

    while len(Q):
        (cost, u) = Q.pop()
        u += 1
        for v in range(1, n):
            if d[v] > d[u] + G[u][v]:
                d[v] = d[u] + G[u][v]
                Q.append((d[v], v))
    return d


def get_path(f, G, s):
    '''
    Восстанавливаем кратчайший путь
    :param f: до куда
    :param G:
    :param s:
    :return:
    '''
    d = __dijkstra(G, s)
