riddle = list(input("give me hugs and kisses: "))

def solve(input: list[str], window_size: int) -> list[list[str]]:
    chunks=[]
    temp=[]
    empty_spaces = 0

    for i in range(len(input)):
        value = input[i]
        
        if value == 'o':
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
print(riddle, '=>', solve(riddle, 3),'\n')
print('\n'*2)
