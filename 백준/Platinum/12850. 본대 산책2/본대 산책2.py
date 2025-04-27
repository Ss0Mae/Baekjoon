def matrix_mul(A, B):
    ans = [[0 for _ in range(len(A))] for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            temp = 0
            for k in range(len(B)):
                temp += A[i][k] * B[k][j]
            ans[i][j] = temp % 1_000_000_007
    return ans

def divide_conquer(A, n):
    if n == 1:
        return A

    else:
        x = divide_conquer(A, n//2)
        if n %2 == 0:
            return matrix_mul(x, x)
        else:
            return matrix_mul(A, matrix_mul(x, x))
        
edges = [
    [0, 1],
    [0, 2],
    [1, 2],
    [1, 3],
    [2, 3],
    [2, 4],
    [3, 4],
    [3, 5],
    [4, 5],
    [4, 7],
    [5, 6],
    [6, 7],
]
graph = [[0 for _ in range(8)] for _ in range(8)]
for i, j in edges:
    graph[i][j] = graph[j][i] = 1

N = int(input())
print(divide_conquer(graph, N)[0][0])