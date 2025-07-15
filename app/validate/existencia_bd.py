from app.models.cadastre import Cadastre 
from app.config.database import Conectar
def cpf_existe_banco_de_dados(cpf:str):
    conexao = Conectar()
    collection = conexao.get_collection()
    
    resultado = collection.find({"usuario_cpf":str(cpf)})
    return resultado is not None
def email_existe_banco_de_dados(email:str):
    conexao = Conectar()
    collection = conexao.get_collection()
    
    resultado = collection.find({"usuario_email":str(email)})
    return resultado is not None