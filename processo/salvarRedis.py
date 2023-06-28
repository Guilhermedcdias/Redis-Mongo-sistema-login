from datetime import datetime
from conection.conect import conect, mongoConect
import os

def salvarRedis(dados):
    conexao = conect()
    chave = dados['tipo']+':'+dados['dados']['cpf']
    print(chave)
    os.system('pause')
    valor = dados['dados']
    valor.pop('_id')
    if 'favoritos' in valor:
        valor.pop('favoritos')
    conexao.hmset(chave, dados['dados'])
    # conexao.hgetall(chave)
    # pegando timestamp da hora atual + 10 minutos
    tempo = int(datetime.timestamp(datetime.now())) + 6000
    conexao.expireat(chave, tempo)
    conexao.close()

    atl = mongoConect()
    db = atl['mercado_livre']
    tipo = dados['tipo']
    col = db[tipo]

    col.update_one({'cpf': dados['dados']['cpf']}, {'$set': {'status': 'logado'}})
    atl.close()