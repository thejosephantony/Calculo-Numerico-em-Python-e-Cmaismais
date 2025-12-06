import numpy as np
import matplotlib.pyplot as plt

def secante(funcao, x0, x1, erro, iteracoes):
    for i in range(1, iteracoes + 1):
        fx0 = funcao(x0)
        fx1 = funcao(x1)
        
        if fx1 - fx0 == 0:
            print("Divisão por zero.")
            return None

        
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0) # formula da secante

        
        if abs(x2 - x1) < erro:                 #parada
            return x2

        
        x0 = x1                                # novos valores
        x1 = x2

    print("Número de iterações acima")
    return None

f = lambda x: x**3 - x - 2

raiz = secante(f, x0=1, x1=2, erro=1e-6, iteracoes=50)
print("Raiz encontrada:", raiz)

xs = np.linspace(-4, 4, 400)
ys = f(xs)

plt.axhline(0, color='black')
plt.plot(xs, ys)
plt.scatter([raiz], [f(raiz)], color='red')
plt.title("Método da Secante - Raiz encontrada")
plt.grid(True)
plt.show()
