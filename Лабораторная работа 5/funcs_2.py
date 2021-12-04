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

