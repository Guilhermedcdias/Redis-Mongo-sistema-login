from menu.login import getTipoUsuario


def dadosLogin(tipo = None):
    if tipo == None:
        table = getTipoUsuario()
    else:
        table = tipo

    if table == '1':
        cpf = input('Digite o cpf: ')
        senha = input('Digite a senha: ')

        return {
            'tipo': 'vendedor',
            'cpf': cpf,
            'senha': senha
        }
    else:
        cpf = input('Digite o cpf: ')
        senha = input('Digite a senha: ')

        return {
            'tipo': 'cliente',
            'cpf': cpf,
            'senha': senha
        }


