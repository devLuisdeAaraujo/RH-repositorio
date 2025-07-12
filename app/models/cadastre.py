from pydantic import BaseModel

class Cadastre(BaseModel):
    usuario_nome : str
    usuario_cpf :int
    usuario_email :str
    usuario_senha : str
    

