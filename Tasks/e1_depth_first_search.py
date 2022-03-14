from typing import Hashable, List
import networkx as nx
from collections import deque


# def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
#     """
#     Do an depth-first search and returns list of nodes in the visited order
#
#     :param g: input graph
#     :param start_node: starting node of search
#     :return: list of nodes in the visited order
#     """
#     path_nodes = []  # полностью сгоревшие узлы
#     visited_nodes = {node: False for node in g.nodes}  # посещенные узлы
#     wait_nodes = []  # очередь из горящих узлов ожидающих поджечь своих соседей
#     wait_nodes.append(start_node)  # добавляем в конец очереди узел / конец справа
#     visited_nodes[start_node] = True  # при добавлении узла в очередь он считается посещенным
#     while wait_nodes:  # пока есть горящие узлы (очередь не пустая) будем зажигать :)
#         current_node = wait_nodes.pop()  # забираем горящий узле с начала очереди
#         neighbours = g[current_node]
#
#         for neighbour in neighbours:
#             if not visited_nodes[neighbour]:
#                 wait_nodes.append(neighbour)
#                 visited_nodes[neighbour] = True
#         path_nodes.append(current_node)  # полностью сожгли
#     return path_nodes
#     print(g, start_node)
#     return list(g.nodes)

from Tasks.e0_breadth_first_search import draw_graph


def dfs(g: nx.Graph, start_node: Hashable):
    """
    от каждого соседа рекурсивно запустить поиск в глубину,
    то есть по факту сосед становится новым стартовым узлом.
    Подумать:
    - что должна возвращать рекурсивная функция
    - какой терминальный случай
    - как контролировать какие узлы уже посещали, чтобы дважды не пройти по тем же узлам
    """
    draw_graph(g)
    path_nodes = []
    visited_nodes = {node: False for node in g.nodes}

    def _dfs(current_node: Hashable):
        path_nodes.append(current_node)
        visited_nodes[current_node] = True

        neighbours = g[current_node]
        for neighbour in neighbours:
            if not visited_nodes[current_node]:
                return _dfs(neighbour)

    _dfs(start_node)

    return path_nodes