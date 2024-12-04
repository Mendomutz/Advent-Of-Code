# def search_x(matrix, word):
#     rows, cols = len(matrix), len(matrix[0])
#     results = []

#     def todas_letras_unicas(diagonal_letras):
#         return len(diagonal_letras) == len(set(diagonal_letras))

#     def limites(x, y):
#         return 0 <= x < rows and 0 <= y < cols

#     def check_x(x, y):
#         # Verifica se o elemento central é "A"
#         if matrix[x][y] != "A":
#             return False

#         # Coordenadas das diagonais
#         diag1 = [(x - 1, y - 1), (x + 1, y + 1)]  # Diagonal principal esquerda cima e direita baixo
#         diag2 = [(x - 1, y + 1), (x + 1, y - 1)]  # Diagonal secundária esquerda baixo e direita cima
#         diag3 = [(x + 1, y - 1), (x - 1, y + 1)]  # Diagonal secundária direita cima e esquerda baixo
#         diag4 = [(x + 1, y + 1), (x - 1, y - 1)]  # Diagonal principal direita baixo e esquerda cima

#         # Verifica se todas as coordenadas das diagonais estão nos limites
#         if not all(limites(nx, ny) for nx, ny in diag1 + diag2 + diag3 + diag4):
#             return False

#         # Coleta as letras das diagonais
#         diag1_letters = [matrix[nx][ny] for nx, ny in diag1]
#         diag2_letters = [matrix[nx][ny] for nx, ny in diag2]
#         diag3_letters = [matrix[nx][ny] for nx, ny in diag3]
#         diag4_letters = [matrix[nx][ny] for nx, ny in diag4]

#         diag1_unicas = todas_letras_unicas(diag1_letters)
#         diag2_unicas = todas_letras_unicas(diag2_letters)
#         diag3_unicas = todas_letras_unicas(diag3_letters)
#         diag4_unicas = todas_letras_unicas(diag4_letters)

#         # Verifica se as letras formam a palavra "MAS" exatamente
#         combined_letters = diag1_letters + diag2_letters + diag3_letters + diag4_letters

#         for i in combined_letters:
#             if i not in word:
#                 return False

#         if not(diag1_unicas and diag2_unicas and diag3_unicas and diag4_unicas):
#             return False

#         return True

#     # Itera sobre cada célula como ponto central do "X"
#     for x in range(rows):
#         for y in range(cols):
#             if check_x(x, y):
#                 results.append((x, y))

#     return results

# # Exemplo de uso
# matrix = [
#     "MMMSXXMASM",
#     "MSAMXMSMSA",
#     "AMXSXMAAMM",
#     "MSAMASMSMX",
#     "XMASAMXAMM",
#     "XXAMMXXAMA",
#     "SMSMSASXSS",
#     "SAXAMASAAA",
#     "MAMMMXMMMM",
#     "MXMXAXMASX"
# ]

# # Converte a matriz para lista de listas
# matrix = [list(row) for row in matrix]

# word = "MAS"
# results = search_x(matrix, word)
# qtd = len(results)

# if results:
#     print(f"A palavra '{word}' forma um 'X' {qtd} vezes na matriz. Pontos centrais:")
#     print(results)
# else:
#     print(f"A palavra '{word}' não forma um 'X' na matriz.")

# (1, 2), (2, 6), (2, 7), (3, 2), (3, 4), (7, 1), (7, 3), (7, 5), (7, 7)

def search(word_search: list[str]) -> int:
    pt2_total = 0
    i = 1
    while i < len(word_search) - 1:
        j = 1
        while j < len(word_search[i]) - 1:
            if word_search[i][j] == "A":
                # get relevant cells
                top_left = word_search[i - 1][j - 1]
                top_right = word_search[i - 1][j + 1]
                bottom_left = word_search[i + 1][j - 1]
                bottom_right = word_search[i + 1][j + 1]

                if (top_left == "S" and bottom_right == "M") or (
                    top_left == "M" and bottom_right == "S"
                ):
                    if (top_right == "S" and bottom_left == "M") or (
                        top_right == "M" and bottom_left == "S"
                    ):
                        pt2_total += 1
            j += 1
        i += 1

    return pt2_total

with open("C:/Projetos/Advent Of Code/2024/puzzle inputs/4.txt", "r") as arquivo:
    matrix = arquivo.read().splitlines()

    print(f"'X-MAS' count: {search(matrix)}")
