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

def calculate_determinant(matrix):
    return np.linalg.det(matrix)

def calculate_inverse(matrix):
    try:
        return np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        return None

# Main Program
print("=== Program Determinan, Invers, dan Perkalian ===")
A = input_matrix("A")

# Determinan
det = calculate_determinant(A)
print(f"\nDeterminan Matriks A: {det:.2f}")

# Invers
inv = calculate_inverse(A)
if inv is not None:
    print("\nInvers Matriks A:")
    print(inv)

    # Perkalian Matriks A * Invers A
    hasil = A @ inv
    print("\nPerkalian Matriks A * Invers A:")
    print(np.round(hasil, 2))  # Dibulatkan agar hasil mendekati identitas
else:
    print("\nMatriks A tidak memiliki invers (determinan = 0 atau singular).")
