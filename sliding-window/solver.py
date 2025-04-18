tests: list[list[int]] = [
    [1,0,0,1,1,1,0,0,0,1],
    [1,0,1],
    [1,1,1,1,0,0,1],
    [1,1,0,0,0,1],
    [1,0,0,1,0,1],
    [1,0,0,0,1,1,1,0,0,0,1],
    [1,0,1,0,0,0,0,1,1,1,1,0,1]
]

def solve(input: list[int], window_size: int) -> list[list[int]]:
    chunks = []
    temp = []
    empty_spaces = 0

    for value in input:        
        if value == 0:
            empty_spaces += 1
            continue
        if empty_spaces >= window_size:
            chunks.append(temp)
            temp = []
        empty_spaces = 0
        temp.append(value)

    if len(temp) > 0:
        chunks.append(temp)

    return chunks

print('\n'*2)
for test in tests:
    print(test, '=>', solve(test, 3),'\n')
print('\n'*2)
