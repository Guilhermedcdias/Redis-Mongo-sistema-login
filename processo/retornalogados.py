from conection.conect import mongoConect


def retornalogados():
    vends = []
    clis = []

    mongo = mongoConect()
    db = mongo['mercado_livre']
    collection = db['vendedor']
    # pegando tudo que o status é logado
    vendedores = collection.find({'status': 'logado'})
    # percorrendo e adicionando o array
    for vendedor in vendedores:
        vends.append(vendedor)
    
    collection = db['cliente']
    # pegando tudo que o status é logado
    clientes = collection.find({'status': 'logado'})
    # percorrendo e adicionando o array
    for cliente in clientes:
        clis.append(cliente)
    
    mongo.close()
    return {
        'vendedores': vends,
        'clientes': clis
    }
