import numpy as np

def input_matrix(name="Matrix"):
    n = int(input(f"Masukkan ukuran matriks {name} (n x n): "))
    print(f"Masukkan elemen-elemen matriks {name} baris per baris (dipisahkan dengan spasi):")
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Baris {i+1}: ").split()))
        if len(row) != n:
            print("Jumlah elemen tidak sesuai! Silakan ulangi.")
            return input_matrix(name)
        matrix.append(row)
    return np.array(matrix)

def inverse_matrix(matrix):
    try:
        inv = np.linalg.inv(matrix)
        return inv
    except np.linalg.LinAlgError:
        return None

# Main Program
print("=== Program Menghitung Invers Matriks ===")
mat = input_matrix("A")

invers = inverse_matrix(mat)

if invers is not None:
    print("\nInvers dari Matriks A adalah:")
    print(invers)
else:
    print("\nMatriks tidak memiliki invers (determinannya nol atau singular).")
