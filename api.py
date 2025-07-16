from fastapi import FastAPI
from app.routes.cadastre import CADASTRE_ROUTER 
from fastapi.middleware.cors import CORSMiddleware
app= FastAPI()
cliente_app = [
    "http://localhost:5173"
]
app.include_router(CADASTRE_ROUTER)
app.add_middleware(
    CORSMiddleware,
    allow_origins=cliente_app,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
