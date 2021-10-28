pi = 3.14159
C1, C2, C3 =  list(map(float,input().split()))
T = 0.5 * C1 * C3
Ci = pi * C3 * C3
Tr = (C1 + C2) / 2.0 * C3
S = C2*C2
R = C1*C2
print("TRIANGULO: %.3lf" % T)
print("CIRCULO: %.3f" % Ci)
print("TRAPEZIO: %.3f" % Tr)
print("QUADRADO: %.3f" % S)
print("RETANGULO: %.3f" % R)
