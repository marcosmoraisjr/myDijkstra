# main.py

import util 
from graph import find_route

def main():
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

    # Solicitar origem e destino ao usuário
    origem = input("Digite o vértice de origem: ").upper()
    destino = input("Digite o vértice de destino: ").upper()

    # Verificar se os vértices informados existem
    if origem not in vertices or destino not in vertices:
        print("Vértice de origem ou destino inválido.")
        return

    # Encontrar o menor caminho
    parents, visited = find_route(origem, destino, vertices, distancias)

    # Gerar o caminho
    path = util.generate_path(parents, origem, destino)

    # Imprimir o caminho colorido
    colored_path = ' → '.join([f"{util.Color.GREEN}{node}{util.Color.END}" if node == origem or node == destino else f"{util.Color.BLUE}{node}{util.Color.END}" for node in path.split(' → ')])
    print(f'Menor caminho de {origem} a {destino}: {colored_path}')
    print('')

if __name__ == "__main__":
    # Exemplo de uso
    util.limpar_tela()
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
    print('       ' + util.Color.GREEN + 'C' + util.Color.END + '-- ' + util.Color.RED + '8' + util.Color.END + ' --' + util.Color.GREEN + 'E' + util.Color.END + '     ')
    print('      /|\      |\    ')
    print('     ' + util.Color.RED + '2' + util.Color.END + ' | \     | ' + util.Color.RED + '3' + util.Color.END + '   ')
    print('    /  |  \    |  \  ')
    print('   ' + util.Color.GREEN + 'A' + util.Color.END + '   ' + util.Color.RED + '7' + util.Color.END + '   ' + util.Color.RED + '4' + util.Color.END + '   ' + util.Color.RED + '6' + util.Color.END + '   ' + util.Color.GREEN + 'F' + util.Color.END + ' ')
    print('    \  |    \  |  /  ')
    print('     ' + util.Color.RED + '5' + util.Color.END + ' |     \ | ' + util.Color.RED + '4' + util.Color.END + '   ')
    print('      \|      \|/    ')
    print('       ' + util.Color.GREEN + 'B' + util.Color.END + '-- ' + util.Color.RED + '8' + util.Color.END + ' --' + util.Color.GREEN + 'D' + util.Color.END + '     ')
    
    print('Neste diagrama:')
    print('Os vértices: A, B, C, D, E e F.')
    print('As linhas entre os vértices representam as arestas.')
    print('Os números ao lado das linhas indicam o peso de cada aresta.')
    print('  A-C (2), A-B (5), C-E (8), C-D (7), C-F (4), B-D (8), E-F (6)')
    print()

    #Instruções de uso:
    #Certifique-se de ter os três arquivos (util.py, graph.py e main.py) no mesmo diretório.
    #Execute o arquivo main.py.
    #Siga as instruções para inserir o vértice de origem e destino quando solicitado.
    #O programa calculará e mostrará o menor caminho entre os vértices informados no grafo definido em graph.py, utilizando os utilitários definidos em util.py.
    main()
