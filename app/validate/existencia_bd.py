
from app.config.database import Conectar
from app.validate.validate import *
conexao = Conectar()
collection = conexao.get_collection()

def cpf_existe_banco_de_dados(cpf: str) -> bool:
    cpf_limpo = limpar_cpf(cpf)
    resultado = collection.find_one({"usuario_cpf": cpf_limpo})
    
    return resultado is not None


def email_existe_banco_de_dados(email: str) -> bool:
    resultado = collection.find_one({"usuario_email": str(email)})
    return resultado is not None

