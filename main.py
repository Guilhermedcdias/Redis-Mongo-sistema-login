import os

from conection.conect import mongoConect
from menu.menu import menu
from menu.login import getDadosLogin
from processo.logar import logar
from processo.salvarRedis import salvarRedis
from processo.cadastrar import dadosCadastro
from processo.retornalogados import retornalogados
from processo.verificaLogins import verificaLogs

while True:
    os.system('cls')
    opcao = menu()
    if opcao == '1':
        dados = getDadosLogin()
        if(dados == '1'):
            dados = dadosCadastro()
        else:
            dadosParaSalvar = logar()
            if dadosParaSalvar != None:
                salvarRedis(dadosParaSalvar)
            
        
    elif opcao == '2':
        dados = retornalogados()
        resultados = verificaLogs(dados)
        for resultado in resultados:
            print(resultado)
        os.system('pause')
        
    elif opcao == '3':
        os.system('cls')
        break
    else:
        print('Opção invalida')
        os.system('pause')