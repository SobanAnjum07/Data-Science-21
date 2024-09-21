import profile


class Matrix:
    pass


def createMatrix(rows, cols):
    m = Matrix()
    m.RowCount = rows
    m.ColumnCount = cols
    m.Data = [[0 for c in range(cols)] for r in range(rows)]
    return m


def inputMatrix(m):
    i = 0
    while i < m.RowCount:
        j = 0
        while j < m.ColumnCount:
            m.Data[i][j] = int(input())
            j += 1
        i += 1
    return


def printMatrix(m):
    i = 0
    while i < m.RowCount:
        j = 0
        while j < m.ColumnCount:
            print(m.Data[i][j], end=" ")
            j += 1
        print()
        i += 1
    return

def isSquareMatrix(m):
    if m.RowCount == m.ColumnCount:
        return True
    else:
        return False

def createIdentityMatrix(rows, cols):
    m = Matrix()
    if rows != cols:
	    raise "It Should have same rows and columns"
    else:
        m.RowCount = rows
        m.ColumnCount = cols
        m.Data = [[0 for c in range(cols)] for r in range(rows)]
        i = 0
        while i < m.RowCount:
            j = 0
            while j < m.ColumnCount:
                if i==j:
                    m.Data[i][j] = 1
                    j += 1
                else:
                    j += 1
            i += 1
    return m

def subtractMatrix(m1, m2):
    if m1.RowCount != m2.RowCount or m1.ColumnCount != m2.ColumnCount:
	    raise "Only matrices with same order can be subtracted"

    r = createMatrix(m1.RowCount, m1.ColumnCount)

    i = 0
    while i < r.RowCount:
        j = 0
        while j < r.ColumnCount:
            r.Data[i][j] = m1.Data[i][j] - m2.Data[i][j]
            j += 1
        i += 1
    return r

def multiplyMatrices(m1,m2):
    if m1.RowCount !=m2.ColumnCount or m1.ColumnCount!= m2.RowCount:
        raise "Rows of 1st Matric Should be equal to column of the 2nd matric"
    multiplied = createMatrix(m1.RowCount, m2.ColumnCount)
    i = 0
    while i <m1.RowCount:
        col = 0
        while col < m2.ColumnCount:
            sum = 0
            row = 0 
            while row < m2.RowCount:
                prod = m2.Data[row][col] * m1.Data[i][row]
                sum = sum + prod
                row += 1
            multiplied.Data[i][col] = sum
            col += 1
        i +=1
    return multiplied

def main():
    
    print("Enter a Matrix you want to check square matrix or not")
    rows_sq = int(input("Enter rows:"))
    cols_sq = int(input("Enter columns:"))
    sq_matrix = createMatrix(rows_sq, cols_sq)
    print("Enter intgers for a Matrix")
    inputMatrix(sq_matrix)
    print("The entered Matrix is")
    printMatrix(sq_matrix)
    square_or_not = isSquareMatrix(sq_matrix)
    print(square_or_not)
    print()

    print("Enter the rows and columns of the identity matric")
    rows = int(input("Enter rows:"))
    cols = int(input("Enter columns:"))
    identity = createIdentityMatrix(rows, cols)
    printMatrix(identity)

    print("enter a matrix you want to SUBTRACT")
    rows_s = int(input("Enter rows:"))
    cols_s = int(input("Enter columns:"))
    s_matrix_1 = createMatrix(rows_s, cols_s)
    s_matrix_2 = createMatrix(rows_s, cols_s)
    print("Enter the integers for the 1st matrix")
    inputMatrix(s_matrix_1)
    print("Enter the integers for the 2nd matrix")
    inputMatrix(s_matrix_2)
    subtracted_matrix = subtractMatrix(s_matrix_1, s_matrix_2)
    print("The subtraction of matrices is:")
    printMatrix(subtracted_matrix)
    print()

    print("Enter a 1st matrix you want to Multiply")
    rows_m_1 = int(input("Enter rows:"))
    cols_m_1 = int(input("Enter columns:"))
    m_matrix_1 = createMatrix(rows_m_1, cols_m_1)
    print("Enter the integers for the 1st matrix")
    inputMatrix(m_matrix_1)
    print("Enter a 2nd matrix you want to Multiply")
    rows_m_2 = int(input("Enter rows:"))
    cols_m_2 = int(input("Enter columns:"))
    m_matrix_2 = createMatrix(rows_m_2, cols_m_2)
    print("Enter the integers for the 2nd matrix")
    inputMatrix(m_matrix_2)
    multiplicated_matrix = multiplyMatrices(m_matrix_1, m_matrix_2)
    print("The multiplication of matrices is:")
    printMatrix(multiplicated_matrix)
    print()

main()