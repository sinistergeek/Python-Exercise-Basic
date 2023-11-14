a_2d = [[1,2,3],[4,5,6],[11,12,14]]
b_2d = [[1,0,1],[1,1,0],[1,1,1]]
c_2d = [[2,0],[0,2]]

def sum_of_diagonal(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i][i]

    return sum


print("sum a_2d ", sum_of_diagonal(a_2d))
print("sum b_2d ", sum_of_diagonal(b_2d))
print("sum c_2d ", sum_of_diagonal(c_2d))
