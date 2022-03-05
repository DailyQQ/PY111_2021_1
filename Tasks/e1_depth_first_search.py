from typing import Hashable, List
import networkx as nx
from collections import deque


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    path_nodes = []  # полностью сгоревшие узлы
    visited_nodes = {node: False for node in g.nodes}  # посещенные узлы
    wait_nodes = []  # очередь из горящих узлов ожидающих поджечь своих соседей
    wait_nodes.append(start_node)  # добавляем в конец очереди узел / конец справа
    visited_nodes[start_node] = True  # при добавлении узла в очередь он считается посещенным
    while wait_nodes:  # пока есть горящие узлы (очередь не пустая) будем зажигать :)
        current_node = wait_nodes.pop()  # забираем горящий узле с начала очереди
        neighbours = g[current_node]

        for neighbour in neighbours:
            if not visited_nodes[neighbour]:
                wait_nodes.append(neighbour)
                visited_nodes[neighbour] = True
        path_nodes.append(current_node)  # полностью сожгли
    return path_nodes
    print(g, start_node)
    return list(g.nodes)
