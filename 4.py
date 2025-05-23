import numpy as np

def input_matrix_3x3(name="Matrix"):
    print(f"Masukkan elemen matriks {name} (3x3), baris per baris:")
    matrix = []
    for i in range(3):
        row = list(map(float, input(f"Baris {i+1}: ").split()))
        if len(row) != 3:
            print("Harus 3 elemen per baris.")
            return input_matrix_3x3(name)
        matrix.append(row)
    return np.array(matrix)

def sarrus_determinant(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    det = (a*e*i + b*f*g + c*d*h) - (c*e*g + b*d*i + a*f*h)
    return det

def minor(matrix, i, j):
    return np.delete(np.delete(matrix, i, axis=0), j, axis=1)

def cofactor_matrix(matrix):
    cof = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            sign = (-1) ** (i + j)
            cof[i][j] = sign * np.linalg.det(minor(matrix, i, j))
    return cof

def inverse_by_cofactor(matrix):
    det = sarrus_determinant(matrix)
    if det == 0:
        return None
    cof = cofactor_matrix(matrix)
    adj = cof.T  # adjoin/transpose
    return adj / det

# === MAIN PROGRAM ===
print("=== Program Sarrus, Kofaktor, dan Perkalian Matriks 3x3 ===")
A = input_matrix_3x3("A")

# Determinan (Sarrus)
det = sarrus_determinant(A)
print(f"\nDeterminan Matriks A (Sarrus): {det:.2f}")

# Invers (Metode Kofaktor)
inv = inverse_by_cofactor(A)
if inv is not None:
    print("\nInvers Matriks A (Metode Kofaktor):")
    print(np.round(inv, 2))

    # Perkalian A * A^-1
    hasil = A @ inv
    print("\nHasil Perkalian A * Invers A (seharusnya mendekati identitas):")
    print(np.round(hasil, 2))
else:
    print("\nMatriks tidak memiliki invers karena determinan = 0.")
