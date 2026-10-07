#Fecha de Realizacion del programa: 26 de Mayo del 2024
#Descripcion: Aqui estan las operaciones que utiliza mi Programa para calcular las matrices

#Operaciones
#Suma, Resta, Multiplicacion y Multiplicacion por escalar

 
#"Aqui se determina el tipo de la matriz dada"
def determine_matrix_type(matrix):
    """
    Determina el tipo de una matriz dada.
    
    Parámetros:
    matrix (list): La matriz para la cual se determina el tipo.
    
    Retorna:
    str: Una descripción del tipo de matriz.
    """
    rows, cols = len(matrix), len(matrix[0])
    if rows == cols:
        if all(matrix[i][j] == 0 for i in range(rows) for j in range(cols) if i != j):
            if all(matrix[i][i] == matrix[0][0] for i in range(rows)):
                return "Matriz Escalar"
            return "Matriz Diagonal"
        return "Matriz Cuadrada"
    elif rows == 1:
        return "Matriz de Fila"
    elif cols == 1:
        return "Matriz de Columna"
    elif all(matrix[i][j] == 0 for i in range(rows) for j in range(cols)):
        return "Matriz Nula"
    else:
        return "Matriz Rectangular"
#Suma
def add_matrices(A, B):
    """
    Suma dos matrices A y B.
    
    Parámetros:
    A (list): Primera matriz.
    B (list): Segunda matriz.
    
    Retorna:
    list: La matriz resultante de la suma de A y B.
    """
    rows, cols = len(A), len(A[0])
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return result

#Resta
def subtract_matrices(A, B):
    """
    Resta la matriz B de la matriz A.
    
    Parámetros:
    A (list): Primera matriz.
    B (list): Segunda matriz.
    
    Retorna:
    list: La matriz resultante de la resta de A y B.
    """
    rows, cols = len(A), len(A[0])
    result = [[A[i][j] - B[i][j] for j in range(cols)] for i in range(rows)]
    return result


#Multiplicacion
def multiply_matrices(A, B):
    """
    Multiplica dos matrices A y B.
    
    Parámetros:
    A (list): Primera matriz.
    B (list): Segunda matriz.
    
    Retorna:
    list: La matriz resultante de la multiplicación de A y B.
    """
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    if cols_A != rows_B:
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B.")
    
    result = [[sum(A[i][k] * B[k][j] for k in range(cols_A)) for j in range(cols_B)] for i in range(rows_A)]
    return result

#Multiplicacion por Escalar
def multiply_matrix_scalar(matrix, scalar):
    """
    Multiplica una matriz por un escalar.
    
    Parámetros:
    matrix (list): La matriz a multiplicar.
    scalar (float): El escalar por el que se multiplica la matriz.
    
    Retorna:
    list: La matriz resultante de la multiplicación por el escalar.
    """
    rows, cols = len(matrix), len(matrix[0])
    result = [[matrix[i][j] * scalar for j in range(cols)] for i in range(rows)]
    return result
