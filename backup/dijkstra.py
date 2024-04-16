import os  # Biblioteca para interagir com funcionalidades dependentes do sistema operacional, como limpar a tela do terminal.
import platform  # Biblioteca para acessar informações sobre o sistema operacional onde o código está sendo executado.

# Util
# Define as cores ANSI
# Util
# Definindo códigos de formatação ANSI para cores
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Util
# Função para limpar a tela do terminal
def limpar_tela():
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows":
        os.system("cls")
    elif sistema_operacional == "Linux":
        os.system("clear")
    else:
        print("Sistema operacional não suportado.")

# Dijkstra: Função para encontrar o caminho mais curto entre origem e destino
def find_route(start, end):
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

# Util
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

    # Gerar o caminho
    path = generate_path(parents, origem, destino)

    # Imprimir o caminho colorido
    colored_path = ' → '.join([f"\033[1;32m{node}\033[0m" if node == origem or node == destino else f"\033[1;34m{node}\033[0m" for node in path.split(' → ')])
    print(f'Menor caminho de {origem} a {destino}: {colored_path}')
    

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

    #print('       C-- 8 --E     ')
    #print('      /|\      |\    ')
    #print('     2 | \     | 3   ')
    #print('    /  |  \    |  \  ')
    #print('   A   7   4   6   F ')
    #print('    \  |    \  |  /  ')
    #print('     5 |     \ | 4   ')
    #print('      \|      \|/    ')
    #print('       B-- 8 --D     ')

    # Imprimir o grafo com vértices e distâncias coloridos
    print("Grafo com vértices e distâncias coloridos:")
    print('       ' + Color.GREEN + 'C' + Color.END + '-- ' + Color.RED + '8' + Color.END + ' --' + Color.GREEN + 'E' + Color.END + '     ')
    print('      /|\      |\    ')
    print('     ' + Color.RED + '2' + Color.END + ' | \     | ' + Color.RED + '3' + Color.END + '   ')
    print('    /  |  \    |  \  ')
    print('   ' + Color.GREEN + 'A' + Color.END + '   ' + Color.RED + '7' + Color.END + '   ' + Color.RED + '4' + Color.END + '   ' + Color.RED + '6' + Color.END + '   ' + Color.GREEN + 'F' + Color.END + ' ')
    print('    \  |    \  |  /  ')
    print('     ' + Color.RED + '5' + Color.END + ' |     \ | ' + Color.RED + '4' + Color.END + '   ')
    print('      \|      \|/    ')
    print('       ' + Color.GREEN + 'B' + Color.END + '-- ' + Color.RED + '8' + Color.END + ' --' + Color.GREEN + 'D' + Color.END + '     ')
    
    print('Neste diagrama:')
    print('Os vértices: A, B, C, D, E e F.')
    print('As linhas entre os vértices representam as arestas.')
    print('Os números ao lado das linhas indicam o peso de cada aresta.')
    print('  A-C (2), A-B (5), C-E (8), C-D (7), C-F (4), B-D (8), E-F (6)')
    print()

    # Exemplo de uso
    # Lista de vértices
    vertices = ('A', 'B', 'C', 'D', 'E', 'F')

    # Dicionário de distâncias entre vértices
    distancias = {
        'A': {'C': 2, 'B': 5},
        'B': {'A': 5, 'D': 8, 'C': 7},
        'C': {'A': 2, 'E': 8, 'D': 4, 'B': 7},
        'D': {'B': 8, 'C': 4, 'E': 6, 'F': 4},
        'E': {'F': 3, 'D': 6, 'C': 8},
        'F': {'D': 4, 'E': 3}
    }

    main()
