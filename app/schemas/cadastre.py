def cadastreEntidade(db_item) -> dict:
    return {
        "id":str(db_item['_id']),
        "nome": db_item['usuario_nome'],
        "cpf": db_item['usuario_cpf'],
        "email" : db_item["usuario_email"],
        "senha": db_item["usuario_senha"]

    }
def listaUsuariosEntidade(db_item_lista) -> list:
    lista_cadastrados= []
    for item in db_item_lista:
        lista_cadastrados.append(cadastreEntidade(item))
    return lista_cadastrados

