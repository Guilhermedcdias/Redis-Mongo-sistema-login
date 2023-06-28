from conection.conect import mongoConect, conect
import os

def verificaLogs(dados):
    user = []
    vendedores = dados['vendedores']
    clientes = dados['clientes']
    redis = conect()
    for vendedor in vendedores:
        stringChave = 'vendedor:'+vendedor['cpf']
        # procurando no redis e verificando se expirou
        verifica = redis.hgetall(stringChave)
        if verifica:
            a = 'Vendedor: '+vendedor['nome']+' logado - cpf: '+vendedor['cpf']
            user.append(a)
        else:
            a = 'Vendedor: '+vendedor['nome']+' deslogado - cpf: '+vendedor['cpf']
            user.append(a)
            mongo = mongoConect()
            db = mongo['mercado_livre']
            collection = db['vendedor']
            collection.update_one({'cpf': vendedor['cpf']}, {'$set': {'status': 'deslogado'}})
            mongo.close()

    
    for cliente in clientes:
        stringChave = 'cliente:'+cliente['cpf']
        # procurando no redis e verificando se expirou
        verifica = redis.hgetall(stringChave)
        if verifica:
            b ='Cliente: '+cliente['nome']+' logado - '+cliente['cpf']
            user.append(b)
        else:
            b = 'Cliente: '+cliente['nome']+' deslogado - '+cliente['cpf']
            user.append(b)
            mongo = mongoConect()
            db = mongo['mercado_livre']
            collection = db['cliente']
            collection.update_one({'cpf': cliente['cpf']}, {'$set': {'status': 'deslogado'}})
            mongo.close()

    redis.close()
    return user