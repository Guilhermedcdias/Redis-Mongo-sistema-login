import redis
import pymongo
from urllib.parse import quote_plus
import os
from dotenv import load_dotenv


def conect():
    load_dotenv()
    host = os.getenv('HOST_REDIS')
    port = os.getenv('PORT_REDIS')
    pswd = os.getenv('PASSWORD_REDIS')
    # iniciando conexao com o redis usando host user e senha
    conexao = redis.Redis(
        host=host,
        port=port,
        password=pswd
    )

    # Executa algumas operações básicas
    conexao.set('conect', 'conectado')  # Define o valor para a chave
    valor = conexao.get('conect')  # Obtém o valor da chave como bytes


    # Converte os bytes para uma string usando o formato de codificação UTF-8
    valor_str = valor.decode('utf-8')
    print(valor_str)  # Imprime a string convertida

    os.system('cls')
    return conexao

def mongoConect():
    load_dotenv()
    pswd = os.getenv('PASSWORD')
    us = os.getenv('us')
    username = quote_plus(us)
    password = quote_plus(pswd)
    cluster = 'guilhermedcdias.4woklyl.mongodb.net'
    uri = 'mongodb+srv://' + username + ':' + password + \
        '@' + cluster + '/?retryWrites=true&w=majority'
    client = pymongo.MongoClient(uri)

    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    os.system('cls')
    
    return client