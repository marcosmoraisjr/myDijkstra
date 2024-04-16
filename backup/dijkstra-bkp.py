import os
import platform

# Função para limpar a tela do terminal
def limpar_tela():
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows":
        os.system("cls")
    elif sistema_operacional == "Linux":
        os.system("clear")
    else:
        print("Sistema operacional não suportado.")

# Função para encontrar o caminho mais curto entre origem e destino
def find_route(start, end):
    unvisited = {node: float('inf') for node in vertices}
    current_distance = 0
    unvisited[start] = current_distance
    visited, parents = {}, {}
    while unvisited:
        min_vertex = min(unvisited, key=unvisited.get)
        for neighbour, distance in distancias[min_vertex].items():
            if neighbour not in unvisited:
                continue
            new_distance = current_distance + distance
            if unvisited[neighbour] is float('inf') or unvisited[neighbour] > new_distance:
                unvisited[neighbour] = new_distance
                parents[neighbour] = min_vertex
        visited[min_vertex] = current_distance
        unvisited.pop(min_vertex)
        if min_vertex == end:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        min_candidate, current_distance = min(candidates, key=lambda x: x[1])
    return parents, visited

# Função para gerar o caminho a partir dos vértices pais
def generate_path(parents, start, end):
    path = [end]
    while True:
        key = parents[path[0]]
        path.insert(0, key)
        if key == start:
            break
    return ' → '.join(path)

# Função principal
def main():

    # Solicitar origem e destino ao usuário
    origem = input("Digite o vértice de origem: ").upper()
    destino = input("Digite o vértice de destino: ").upper()

    # Verificar se os vértices informados existem
    if origem not in vertices or destino not in vertices:
        print("Vértice de origem ou destino inválido.")
        return

    # Encontrar o menor caminho
    parents, visited = find_route(origem, destino)

    # Gerar e imprimir o caminho
    path = generate_path(parents, origem, destino)
    print(f'Menor caminho de {origem} a {destino}: {path}')
    
if __name__ == "__main__":
    # Exemplo de uso
    limpar_tela()
    print('')
    print('Vamos representar o grafo dado de forma linear e explicar cada parte:')
    print('')
    print('Representação Linear:')
    print(' - O grafo pode ser representado linearmente como uma lista de arestas.')
    print('   Cada aresta é indicada por um par de vértices conectados e o peso associado a essa aresta.')
    print('   Aqui está uma representação:')
    print('')
    print('   A -1- B       ')
    print('   |    / \      ')
    print('   4   2   5     ')
    print('   |  /     \    ')
    print('   C ----1-- D   ')
    print('')
    print('Neste diagrama:')
    print('Os vértices: A, B, C e D.')
    print('As linhas entre os vértices representam as arestas.')
    print('Os números ao lado das linhas indicam o peso de cada aresta.')
    print('')
    print('A representação linear seria:')
    print('A-B (1), A-C (4), B-C (2), B-D (5), C-D (1)')
    print()

    # Exemplo de uso
    # Lista de vértices
    vertices = ('A', 'B', 'C', 'D')

    distancias = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    # Dicionário de distâncias entre vértices
    distancias2 = {
        'A': {'C': 2, 'B': 5},
        'B': {'A': 5, 'D': 8, 'C': 7},
        'C': {'A': 2, 'E': 8, 'D': 4, 'B': 7},
        'D': {'B': 8, 'C': 4, 'E': 6, 'F': 4},
        'E': {'F': 3, 'D': 6, 'C': 8},
        'F': {'D': 4, 'E': 3}
    }
    
    main()
