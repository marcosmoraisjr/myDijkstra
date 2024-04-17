def get_user_input():
    vertices = set()
    distancias = {}

    while True:
        entrada = input("Digite o vértice no formato X-Y (ou 'parar' para encerrar): ").strip().upper()

        if entrada == 'PARAR':
            break

        if '-' not in entrada or len(entrada) != 3:
            print("Formato inválido. Por favor, digite no formato correto (por exemplo, A-C).")
            continue

        x, y = entrada.split('-')
        distancia = int(input(f"Digite a distância entre os vértices {x} e {y}: "))

        # Adicionar vértices ao conjunto de vértices
        vertices.add(x)
        vertices.add(y)

        # Adicionar distância ao dicionário de distâncias
        if x not in distancias:
            distancias[x] = {}
        if y not in distancias:
            distancias[y] = {}
        distancias[x][y] = distancia
        distancias[y][x] = distancia

    return tuple(sorted(vertices)), distancias

# Exemplo de uso
#vertices, distancias = get_user_input()
#print("Vertices:", vertices)
#print("Distancias:", distancias)
