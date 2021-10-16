n = int(input('Digite quantos números de Fibonacci você desaja: '))
anterior = 0
atual = 1
cont = 1
while (cont <= n):
    posterior = anterior + atual
    print('{}º - {}'.format(cont, posterior))
    cont += 1
    anterior = atual
    atual = posterior
print('Fim')