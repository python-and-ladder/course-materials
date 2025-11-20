# Bitwise Operators
p = 5  # 0101 in binary
q = 3  # 0011 in binary
print("AND:", p & q)                  # 1 (0001)
print("OR:", p | q)                   # 7 (0111)
print("XOR:", p ^ q)                  # 6 (0110)
print("NOT:", ~p)                     # -6 (inverts bits)
print("Left Shift:", p << 1)         # 10 (1010)
print("Right Shift:", p >> 1)       # 2 (0010)
