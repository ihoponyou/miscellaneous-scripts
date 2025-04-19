
def sum_2d_arr(arr: list[list[int]]) -> int:
    return sum(map(sum, arr))

outcomes = [
    [11,13,9],
    [32,28,27],
    [7,9,14],
]
expected = [[0]*len(x) for x in outcomes]
contributions = [[0]*len(x) for x in outcomes]

def calculate_column_total(matrix: list[list[int]], j: int) -> int:
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][j]
    return sum

def calculate_eij(matrix: list[list[int]], i: int, j: int, n: int) -> int:
    row = matrix[i]
    row_total = sum(row)
    column_total = calculate_column_total(matrix, j)
    return int((row_total * column_total) / n)

for i in range(len(outcomes)):
    for j in range(len(outcomes[i])):
        expected[i][j] = calculate_eij(outcomes, i, j, sum_2d_arr(outcomes))

for i in range(len(outcomes)):
    for j in range(len(outcomes[i])):
        contributions[i][j] = (outcomes[i][j] - expected[i][j]) ** 2 / expected[i][j]

sample_variance = sum_2d_arr(contributions)
print(sample_variance)