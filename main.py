# main.py

import util 
from graph import find_route
from input import get_user_input

def main():
    # Opção para o usuário inserir as cidades e distâncias manualmente ou não
    opcao = input("Deseja inserir as cidades e distâncias manualmente? (s/n): ").lower()
    if opcao == 's':
        # Se o usuário optar por inserir manualmente, obtenha as cidades e distâncias
        vertices, distancias = get_user_input()
    else:
        # Use o grafo padrão
        vertices = ('A', 'B', 'C', 'D', 'E', 'F')

        distancias = {
            'A': {'C': 2, 'B': 5},
            'B': {'A': 5, 'D': 8, 'C': 7},
            'C': {'A': 2, 'E': 8, 'D': 4, 'B': 7},
            'D': {'B': 8, 'C': 4, 'E': 6, 'F': 4},
            'E': {'F': 3, 'D': 6, 'C': 8},
            'F': {'D': 4, 'E': 3}
        }

    # Restante do seu código permanece o mesmo

if __name__ == "__main__":
    # Exemplo de uso
    util.limpar_tela()
    # Restante do seu código permanece o mesmo
# main.py

import util 
from graph import find_route
from input import get_user_input

def main():
    # Opção para o usuário inserir as cidades e distâncias manualmente ou não
    opcao = input("Deseja inserir as cidades e distâncias manualmente? (s/n): ").lower()
    if opcao == 's':
        # Se o usuário optar por inserir manualmente, obtenha as cidades e distâncias
        vertices, distancias = get_user_input()
    else:
        # Use o grafo padrão
        vertices = ('A', 'B', 'C', 'D', 'E', 'F')

        distancias = {
            'A': {'C': 2, 'B': 5},
            'B': {'A': 5, 'D': 8, 'C': 7},
            'C': {'A': 2, 'E': 8, 'D': 4, 'B': 7},
            'D': {'B': 8, 'C': 4, 'E': 6, 'F': 4},
            'E': {'F': 3, 'D': 6, 'C': 8},
            'F': {'D': 4, 'E': 3}
        }

    #print("Vertices:\n", vertices, "\n") 
    #print("Distancias:\n", distancias)

    # Solicitar origem e destino ao usuário
    origem = input("Digite o vértice de origem: ").upper()
    destino = input("Digite o vértice de destino: ").upper()

    # Verificar se os vértices informados existem
    if origem not in vertices or destino not in vertices:
        print("Vértice de origem ou destino inválido.")
        return

    # Encontrar o menor caminho
    parents, visited = find_route(origem, destino, vertices, distancias)
    print(parents) 
    print(visited)
    
    # Gerar o caminho
    path = util.generate_path(parents, origem, destino)

    # Imprimir o caminho colorido
    colored_path = ' → '.join([f"{util.Color.GREEN}{node}{util.Color.END}" if node == origem or node == destino else f"{util.Color.BLUE}{node}{util.Color.END}" for node in path.split(' → ')])
    print('')
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
    print('  A-C (2), A-B (5), C-B (7), C-D (4), C-E (8), D-E (6), D-F (4), E-F (3)')
    print()

    #Instruções de uso:
    #Certifique-se de ter os três arquivos (util.py, graph.py e main.py) no mesmo diretório.
    #Execute o arquivo main.py.
    #Siga as instruções para inserir o vértice de origem e destino quando solicitado.
    #O programa calculará e mostrará o menor caminho entre os vértices informados no grafo definido em graph.py, utilizando os utilitários definidos em util.py.
    main()
