import numpy as np
import matplotlib.pyplot as plt

# o metodo de newton usa a reta tangente

def MetodoNewton(funcaoF, derivadaF, x0, e, iteracoes):
    x = x0
    
    for i in range(1, iteracoes + 1):

        
        if derivadaF(x) == 0:                # aqui verifica se a derivada é zero, caso seja o metodo não funciona
            print("A derivada é zero.\n")
            return None

                                            
        x1 = x - funcaoF(x) / derivadaF(x)  # formula de Newton

        
        if abs(x1 - x) < e:               #parada
            return x1

        x = x1

    print("Número de iterações excedido.\n")
    return None

funcaoF  = lambda x: x**3 - x - 2
derivadaF = lambda x: 3*x**2 - 1

raiz = MetodoNewton(funcaoF, derivadaF, x0=1.5, e=1e-6, iteracoes=20)
print("Raiz: \n", raiz)


# gráfico
xs = np.linspace(-4, 4, 400)
ys = funcaoF(xs)

plt.axhline(0, color='black')
plt.plot(xs, ys)
plt.scatter([raiz], [funcaoF(raiz)], color='red')
plt.title("Função e raiz encontrada pelo Método de Newton")
plt.grid(True)
plt.show()