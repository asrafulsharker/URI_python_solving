L1 = input().split(" ")
L2 = input().split(" ")
A1, B1, C1 = L1
A2, B2, C2 = L2
total = (int(B1) * float(C1)) + (int(B2) * float(C2))
print(f'VALOR A PAGAR: R$ {total:.2f}')
