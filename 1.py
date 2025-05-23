import numpy as np

def input_matrix(name="Matrix"):
    rows = int(input(f"Masukkan jumlah baris untuk {name}: "))
    cols = int(input(f"Masukkan jumlah kolom untuk {name}: "))
    print(f"Masukkan elemen {name} baris per baris, dipisahkan dengan spasi:")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Baris {i+1}: ").split()))
        if len(row) != cols:
            print("Jumlah elemen tidak sesuai kolom! Silakan ulangi.")
            return input_matrix(name)
        matrix.append(row)
    return np.array(matrix)

def add_matrices(A, B):
    return A + B

def subtract_matrices(A, B):
    return A - B

def multiply_matrices(A, B):
    return A @ B

# Main Program
print("=== Program Operasi Matriks ===")
matrixA = input_matrix("Matriks A")
matrixB = input_matrix("Matriks B")

if matrixA.shape != matrixB.shape:
    print("Penjumlahan dan pengurangan tidak bisa dilakukan: ukuran matriks tidak sama.")
else:
    print("\nHasil Penjumlahan:")
    print(add_matrices(matrixA, matrixB))

    print("\nHasil Pengurangan:")
    print(subtract_matrices(matrixA, matrixB))

try:
    print("\nHasil Perkalian:")
    print(multiply_matrices(matrixA, matrixB))
except ValueError as e:
    print("Perkalian tidak bisa dilakukan:", e)
