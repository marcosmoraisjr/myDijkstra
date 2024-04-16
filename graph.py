# graph.py

# Dijkstra: Função para encontrar o caminho mais curto entre origem e destino
def find_route(start, end, vertices, distancias):
    # Inicialização dos vértices não visitados com distância infinita
    unvisited = {node: float('inf') for node in vertices}
    current_distance = 0
    unvisited[start] = current_distance
    visited, parents = {}, {}
    while unvisited:
        # Encontrar o vértice não visitado mais próximo
        min_vertex = min(unvisited, key=unvisited.get)
        # Percorrer os vizinhos do vértice atual
        for neighbour, distance in distancias[min_vertex].items():
            if neighbour not in unvisited:
                continue
            # Calcular a nova distância até o vizinho
            new_distance = current_distance + distance
            # Atualizar a distância se for menor
            if unvisited[neighbour] is float('inf') or unvisited[neighbour] > new_distance:
                unvisited[neighbour] = new_distance
                parents[neighbour] = min_vertex
        # Marcar o vértice atual como visitado
        visited[min_vertex] = current_distance
        unvisited.pop(min_vertex)
        # Parar se alcançar o destino
        if min_vertex == end:
            break
        # Atualizar o vértice atual e a distância atual
        candidates = [node for node in unvisited.items() if node[1]]
        min_candidate, current_distance = min(candidates, key=lambda x: x[1])
    return parents, visited
