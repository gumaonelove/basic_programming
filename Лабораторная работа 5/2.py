'''
Постройте граф, моделирующий дорожную сеть, на основе данных фрагмента карты (например, 2ГИС или Яндекс.Карты) любой
местности по Вашему выбору с числом вершин не менее 15.
Постройте с пользователем диалог таким образом, чтобы он мог запрашивать у программы информацию о кратчайшем расстоянии
между двумя пунктами карты (вершинами графа), при этом получал на экране информацию о кратчайшем расстоянии и путь.
Граф должен быть задан в табличной форме в виде матрицы смежности в файле.
'''

from funcs_2 import get_graph, get_list_address

G = get_graph()

addresses = get_list_address()
print('Список доступных адреса:', addresses, sep='\n')

start_address = input('Введите адрес старта: ')
finish_address = input('Введите адрес финиша: ')

