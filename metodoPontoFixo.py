import numpy as np

import matplotlib.pyplot as plt

def pontoFixo(g, x0, erro, iteracoes):
    for i in range(iteracoes):
        x1 = g(x0)

        if abs(x1 - x0) < erro: 
            return x1

        x0 = x1

    print("iteracoes excedida")
    return None

g = lambda x: np.log(10/x)

raiz = pontoFixo(g, x0=2, erro=1e-6, iteracoes=50)
print("Raiz encontrada:", raiz)

xs = np.linspace(0.1, 6, 400)   
ys = g(xs)

plt.axhline(0, color='black')
plt.plot(xs, ys)
plt.scatter([raiz], [g(raiz)], color='red')
plt.title("Método do Ponto Fixo - Raiz encontrada")
plt.grid(True)
plt.show()
