
import os
from conection.conect import mongoConect
from processo.logar import logar
from processo.salvarRedis import salvarRedis
from menu.login import getTipoUsuario

def dadosCadastro():
    table = getTipoUsuario()

    if table == '1':
        cpf = input('Digite o cpf: ')
        
        conexao = mongoConect()

        db = conexao['mercado_livre']
        collection = db['vendedor']
        vendedor = collection.find_one({'cpf': cpf})

        if vendedor == None:
            print('Vendedor não existe')
            os.system('pause')
        else:
            senha = input('Digite a senha: ')
            collection.update_one({'cpf': cpf}, {'$set': {'senha': senha}})
            print('Senha cadastrada com sucesso')
            os.system('pause')
            dadosParaSalvar = logar('1')
            if dadosParaSalvar != None:
                salvarRedis(dadosParaSalvar)
            
        
        conexao.close()
    else:
        cpf = input('Digite o cpf: ')

        conexao = mongoConect()

        db = conexao['mercado_livre']
        collection = db['cliente']
        cliente = collection.find_one({'cpf': cpf})

        if cliente == None:
            print('Cliente não existe')
            os.system('pause')
        else:
            senha = input('Digite a senha: ')
            collection.update_one({'cpf': cpf}, {'$set': {'senha': senha}})
            print('Senha cadastrada com sucesso')
            os.system('pause')
            dadosParaSalvar = logar('2')
            if dadosParaSalvar != None:
                salvarRedis(dadosParaSalvar)
        
        conexao.close()