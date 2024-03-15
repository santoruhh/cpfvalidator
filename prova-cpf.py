"""
Validador de CPF
"""

cpf = input('CPF: ')
multiplicador = 10
indice = 0
qtd_num_cpf = cpf[0:9]
lista = []

for item in qtd_num_cpf:

    item = int(item) * multiplicador
    multiplicador -= 1
    lista.append(item)
   
soma_da_lista = 0

for numero in lista:

    soma_da_lista += numero

resultado_cpf = soma_da_lista * 10
resto = resultado_cpf % 11

primeiro_digito = 0 if resto > 9 else resto

# segundo digito

multiplicador2 = 11
qtd_num_cpf2 = cpf[0:10]
lista2 = []

for item2 in qtd_num_cpf2:

    item2 = int(item2) * multiplicador2
    multiplicador2 -= 1
    lista2.append(item2)
   
soma_da_lista2 = 0

for numero2 in lista2:

    soma_da_lista2 += numero2

resultado_cpf2 = soma_da_lista2 * 10
resto2 = resultado_cpf2 % 11

segundo_digito = 0 if resto2 > 9 else resto2


if primeiro_digito == int(cpf[9])\
    and segundo_digito == int(cpf[10]):

    print('O CPF digitado é valido.')

else:
    
    print('CPF Inválido.')