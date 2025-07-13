from validate_docbr import CPF
import regex as re
import hashlib
def validar_cpf(cpf:int)->bool:
    validacao_cpf = CPF()
    return validacao_cpf.validate(cpf)
def validar_email(emaiL:str)-> bool:
    validacao_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return (re.match(validacao_email,emaiL))
def verificar_senha(senha:str)->bool:
        minimo_senha = 8
        letras_maiusculas = 1
        letras_minusculas = 1
        numeros_minimo = 1

        count_caracter_especial = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', senha))
        count_numeros = len(re.findall(r'\d', senha))
        count_letras_maiuscula = len(re.findall(r'[A-Z]', senha))
        count_letras_minusculas = len(re.findall(r'[a-z]', senha))
        

        if (
            len(senha) >= minimo_senha and
            count_caracter_especial >= 1 and
            count_numeros >= numeros_minimo and
            count_letras_maiuscula >= letras_maiusculas and
            count_letras_minusculas >= letras_minusculas
        ):
            return True
        else:
            return False
        
def senha_criptografada(senha):
        return hashlib.sha256(senha.encode()).hexdigest()