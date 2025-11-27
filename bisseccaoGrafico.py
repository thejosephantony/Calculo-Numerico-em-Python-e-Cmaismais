import numpy as np
import matplotlib.pyplot as plt

def bisseccao(funcao, a, b, eps, interacoes):
    fa = funcao(a)

    for i in range(interacoes):
        c = (a + b) / 2
        fc = funcao(c)

        if fc == 0 or (b - a) / 2 < eps:
            return c

        if fa * fc > 0:
            a = c
            fa = fc
        else:
            b = c

    raise Exception("Número de iterações excedido")


def f(x):
    return x**3 - x - 2            #função que quero encontrar a raiz



a = 1
b = 2
eps = 0.01
max_iter = 100

raiz = bisseccao(f, a, b, eps, max_iter)
print("Raiz aproximada:", raiz)



# Gráfico da função
X = np.linspace(a-1, b+1, 400)
Y = f(X)

plt.figure(figsize=(8, 5))
plt.axhline(0, color='black', linewidth=1)  # eixo x
plt.plot(X, Y, label="f(x) = x³ - x - 2")

# marca a raiz
plt.scatter([raiz], [f(raiz)], color='red', label=f"Raiz ≈ {raiz:.4f}")

plt.title("Método da Bissecção – Gráfico da Função")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
