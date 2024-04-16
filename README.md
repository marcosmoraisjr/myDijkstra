
# myDijkstra

O projeto myDijkstra implementa o algoritmo de Dijkstra para encontrar o caminho mais curto entre dois vértices em um grafo. O código é escrito em Python e pode ser utilizado para diversos propósitos, como roteamento em redes de computadores, navegação GPS e planejamento de viagens.

![Artigo LinkedIn - 1200 x 627 - Dijkstra](https://github.com/marcosmoraisjr/myDijkstra/assets/26969915/fc4ba445-800b-418c-951e-019e59781df9)

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

### 📋 Pré-requisitos

Você precisa ter o Python instalado em sua máquina. Se não tiver, pode baixá-lo e instalá-lo a partir do site oficial: [Python Downloads](https://www.python.org/downloads/).

### 🔧 Instalação

Para obter uma cópia deste projeto, você pode clonar este repositório executando o seguinte comando em seu terminal:

1. Clone o repositório:
```bash
git clone https://github.com/marcosmoraisjr/myDijkstra.git
```
2. Acesse o diretório do projeto:
```bash
d:\>cd marcosmoraisjr\dev\myDijkstra
```
3. Instale as dependências (quando for o caso):
```bash
pip install -r dependencias.txt
```
## ⚙️ O Código

Vamos dividir o código em três arquivos Python separados: um para as definições de utilitários e funções, outro para a definição do grafo e a lógica principal, e um terceiro para o código de execução principal.

*  util.py (para as definições de utilitários e funções):
```python
# util.py

import os
import platform

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

# Função para limpar a tela do terminal
def limpar_tela():
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows":
        os.system("cls")
    elif sistema_operacional == "Linux":
        os.system("clear")
    else:
        print("Sistema operacional não suportado.")

# Função para gerar o caminho a partir dos vértices pais
def generate_path(parents, start, end):
    path = [end]
    while True:
        key = parents[path[0]]
        path.insert(0, key)
        if key == start:
            break
    return ' → '.join(path)
```

* graph.py (para a definição do grafo e a lógica principal):
```python
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
```

*  main.py (para o código de execução principal):
```python
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

    print(' ')
    print('       C-- 8 --E     ')
    print('      /|\      |\    ')
    print('     2 | \     | 3   ')
    print('    /  |  \    |  \  ')
    print('   A   7   4   6   F ')
    print('    \  |    \  |  /  ')
    print('     5 |     \ | 4   ')
    print('      \|      \|/    ')
    print('       B-- 8 --D     ')
    print(' ') 

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

if __name__ == "__main__":
    # Exemplo de uso
    util.limpar_tela()
    main()
```

Aqui está uma explicação simplificada do projeto dividido em três partes:

* 'util.py': Este arquivo contém funções utilitárias que são úteis em todo o projeto. Ele define uma classe Color para fornecer códigos de formatação ANSI para cores no terminal, e também uma função limpar_tela() para limpar a tela do terminal e uma função generate_path() para gerar o caminho a partir dos vértices pais.

* 'graph.py': Neste arquivo, implementamos o algoritmo de Dijkstra para encontrar o menor caminho em um grafo ponderado. A função find_route() recebe um vértice de origem e um vértice de destino, juntamente com a definição do grafo (vértices e distâncias entre eles), e retorna o menor caminho e a distância percorrida. Este arquivo também contém a definição do grafo e das distâncias entre os vértices.

* 'main.py': Este é o arquivo principal do projeto. Ele solicita ao usuário um vértice de origem e um vértice de destino, verifica se são válidos, e em seguida, utiliza as funções definidas em util.py e graph.py para encontrar e exibir o menor caminho entre os vértices informados.

Em resumo, o projeto consiste em uma implementação do algoritmo de Dijkstra para encontrar o menor caminho em um grafo ponderado, com funções utilitárias para limpar a tela do terminal e formatar a saída do resultado.


## ⚙️ Executando o Código
1.Execute o script principal:
```bash
python main.py
```

2. Siga as instruções na tela para inserir os vértices de origem e destino.

3. O programa exibirá o menor caminho entre os vértices informados, com as distâncias e os vértices intermediários.

Para executar os testes automatizados, você pode seguir as instruções no arquivo de código.

## 🛠️ Construído com

Este projeto foi construído com:

* Python

## 📦 Implantação

O projeto pode ser implantado em um servidor web para ser utilizado em um ambiente de produção. Para mais informações sobre como implantar o projeto, consulte a documentação.

## 🛠️ Construído com

* Python

## 📌 Versão

A versão atual do projeto é 1.0.0. Para verificar as versões disponíveis, consulte as tags no repositório do GitHub: https://github.com/marcosmoraisjr/myDijkstra

## ✒️ Autores

* **Marcos Morais** - *Trabalho Inicial* - [marcosmoraisjr](https://github.com/marcosmoraisjr)

Você também pode ver a lista de todos os [colaboradores](https://github.com/marcosmoraisjr/myDijkstra/graphs/contributors) que participaram deste projeto.

## 📄 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](https://github.com/marcosmoraisjr/myDijkstra/blob/main/LICENSE) para detalhes.

## 🖇️ Agradecimentos

* Conte a outras pessoas sobre este projeto 📢;
* Agradeço a todos pelas contribuições futuras cooperando para a evolução deste projeto.

## 🎁 Recursos Adicionais

* Algoritmo de Dijkstra: https://akiradev.netlify.app/posts/algoritmo-dijkstra/;
* Wikipedia - Algoritmo de Dijkstra: https://pt.wikipedia.org/wiki/Algoritmo_de_Dijkstra;
* GeeksforGeeks - Dijkstra's Algorithm: https://www.geeksforgeeks.org/videos/dijkstras-shortest-path-algorithm/.

## 🏆 Agradecimentos
* Conte a outras pessoas sobre este projeto 📢;
* Agradeço a todos que contribuíram para o desenvolvimento deste projeto.
* Agradeço especialmente ao meu estimado professor no mestrado [João B. Rocha-Junior](https://pgcc.uefs.br/sobre/docentes/joao), Doutor em em Ciência da Computação, NTNU, Noruega, pelos ensinamentos.
