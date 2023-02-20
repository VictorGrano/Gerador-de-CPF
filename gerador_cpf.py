import random
import os

def pontua_cpf(cpf):
    cpf_pontuado = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:]
    return cpf_pontuado
def gera_cpf():
    cpf = ''
    for i in range(9):
        cpf += str(random.randint(0, 9))
    contador1 = 10
    resultado_digito1 = 0
    for num in cpf:
        resultado_digito1 += int(num) * contador1
        contador1 -= 1
    digito1 = (resultado_digito1 * 10) % 11
    digito1 = digito1 if digito1 <= 9 else 0
    cpf = cpf + str(digito1)
    contador2 = 11
    resultado_digito2 = 0
    for num in cpf:
        resultado_digito2 += int(num) * contador2
        contador2 -= 1
    digito2 = (resultado_digito2 * 10) % 11
    digito2 = digito2 if digito2 <= 9 else 0
    cpf = cpf + str(digito2)
    cpf_final = pontua_cpf(cpf)
    print(cpf_final)
    return cpf_final
print('Bem vindo ao gerador de cpf!')
while True:
    print('Digite uma opção: \n 1 - Gerar CPF com pontuação / 2 - Gerar CPF em massa / 3 - Sair')
    opc = input('')
    
    if opc == '1':
        os.system('cls')
        gera_cpf()
        continue
    if opc == '2':
        verifica = False
        while verifica == False:
            qtd = input('Digite a quantidade de CPFs para gerar: ')
            try:
                qtd = int(qtd)
                verifica = True
            except:
                print('Digite um número!')
                continue
        os.system('cls')
        for _ in range(qtd):
           gera_cpf()
        continue
    if opc == '3':
        break
    else:
        print('Digite uma opção válida!')
        continue
