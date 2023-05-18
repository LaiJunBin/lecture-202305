arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def spiral_clean_solution(arr):
    output = []

    while len(arr) > 0:
        output.extend(arr.pop(0))
        arr = list(zip(*arr))[::-1]

    return output

def spiral(arr):
    output = []
    
    si, sj, ei, ej = 0, 0, len(arr) - 1, len(arr[0]) - 1
    r = 0
    while si <= ei and sj <= ej:
        o = r % 4
        if o == 0:
            for k in range(sj, ej + 1):
                output.append(arr[si][k])
            si += 1
        elif o == 1:
            for k in range(si, ei + 1):
                output.append(arr[k][ej])
            ej -= 1
        elif o == 2:
            for k in range(ej, sj - 1, -1):
                output.append(arr[ei][k])
            ei -= 1
        else:
            for k in range(ei, si - 1, -1):
                output.append(arr[k][sj])
            sj += 1
        r += 1


    return output
        

output = spiral(arr)
print(output)
