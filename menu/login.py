import os


def getTipoUsuario():
    print('-'*30)
    print('1 - Vendedor')
    print('2 - Cliente')
    print('-'*30)

    valor = input('Digite a opção desejada: ')

    if(valor == '1' or valor == '2'):
        return valor
    else:
        print('Opção invalida')
        os.system('pause')
        return getTipoUsuario()
    

def getDadosLogin():
    print('-'*30)
    print('1 - É Primeiro Login')
    print('2 - Não é meu primeiro login')
    print('-'*30)

    valor = input('Digite a opção desejada: ')

    if(valor == '1' or valor == '2'):
        return valor
    else:
        print('Opção invalida')
        os.system('pause')
        return getDadosLogin()