size_of_table = int(input())
mat = [[1 for x in range(size_of_table)] for y in range(size_of_table)]
for i in range(1, size_of_table):
    for j in range(1, size_of_table):
        mat[i][j] = mat[i - 1][j] + mat[i][j - 1]
print(mat[size_of_table - 1][size_of_table - 1])
