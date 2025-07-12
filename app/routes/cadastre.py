from fastapi import APIRouter,HTTPException
from app.config.database import Conectar
from app.models.cadastre import Cadastre  
from app.schemas.cadastre import *
from pymongo.errors import *


CADASTRE_ROUTER= APIRouter()
conexao = Conectar()
collection = conexao.get_collection()
@CADASTRE_ROUTER.get("/")
async def inicio():
    return "Bem vindo ao RH"
@CADASTRE_ROUTER.get("/cadastro")
async def lista_cadastro():
    resultado = collection.find()
    return listaUsuariosEntidade(resultado)
@CADASTRE_ROUTER.get("/cadastro/{id_jogador}")
async def buscar_usuario_pelo_id(id_jogador:int):
    buscar = collection.find_one({"_id":id_jogador})
    if not buscar:
        return {"mensagem":"Usuario nao cadastrado"}
    return listaUsuariosEntidade(collection.find(buscar))
@CADASTRE_ROUTER.post("/cadastra_usuario/{id_jogador}")
async def cadastrar_usuario(id_jogador:int,usuario:Cadastre):
    usuario_dict = usuario.dict()
    usuario_dict["_id"]=id_jogador
    try:
        resultado = collection.insert_one(usuario_dict)
        return listaUsuariosEntidade(collection.find())
    except DuplicateKeyError:
        raise HTTPException(status_code=400,detail="Document with this ID already exists.")