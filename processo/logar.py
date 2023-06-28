from conection.conect import mongoConect
from processo.pegardados import dadosLogin
from menu.login import getTipoUsuario
import os

def logar(tipo = None):
    if tipo == None:
        tabela = getTipoUsuario()
    else:
        tabela = tipo
    
    dados = dadosLogin(tabela)
    conect = mongoConect()

    db = conect['mercado_livre']
    if (dados['tipo'] == 'vendedor'):
        collection = db['vendedor']
        pessoa = collection.find_one({'cpf': dados['cpf'], 'senha': dados['senha']})

        if pessoa == None:
            print('cpf ou senhas incorretos')
            os.system('pause')
        else:
            conect.close()
            return {
                'tipo': 'vendedor',
                'dados': pessoa
            }
    else:
        collection = db['cliente']
        collection.find_one({'cpf': dados['cpf'], 'senha': dados['senha']})
        pessoa = collection.find_one({'cpf': dados['cpf'], 'senha': dados['senha']})

        if pessoa == None:
            print('cpf ou senhas incorretos')
        else:
            conect.close()
            return {
                'tipo': 'cliente',
                'dados': pessoa
            }
        
    conect.close()