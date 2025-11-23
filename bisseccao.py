# O metodo da bisseccao usa o método numérico para aproximar a raiz de uma função contínua em um intervalo [a, b].

#comentarios (ou não) :(


def bisseccao(funcao, a, b, ε, interacoes): # funcao é a função continua a ser avaliada, a e b são os limites do intervalo fechado, ε é a precisão desejada e interacoes é o número máximo de iterações permitidas.
    i = 1                                   # inicializa o contador de interações
    fa = funcao(a)                          # calcula o valor da funcao no ponto a
    fb = funcao(b)                          # calcula o valor da funcao no ponto b
    while(i <= interacoes):                 # o loop roda enquanto o número de iterações for menor ou igual ao máximo permitido
        c = a + (b-a)/2                     # calcula o ponto medio no intervalo
        fc = funcao(c)                      # calcula o valor da funcao no ponto medio
        if((fc == 0) or ((b-a)/2 < ε)):     # verifica se o valor da funcao no ponto medio é zero ou se a precisão desejada foi alcançada
            return c                        # retorna o ponto medio como a raiz
        i = i + 1                           # vai para a prox interacao
        if((fa * fc > 0)):                  # verifica em qual subintervalo a raiz está localizada
            a = c                           # atualiza o limite inferior do intervalo
            fa = fc                         # atualiza o valor da funcao no novo limite inferior
        else:                               # atualiza o limite superior do intervalo
            b = c                           # atualiza o limite superior do intervalo
    return print("Número de iterações excedido")        # retorna uma mensagem se o número máximo de iterações for excedido


print(bisseccao(lambda x: x**3 - x - 2, 1, 2, 0.01, 100))   # entrada kkk