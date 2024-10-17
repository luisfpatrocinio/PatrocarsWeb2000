from typing import Annotated
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sqlmodel import SQLModel

from patrocarsweb.models import Montadora
from .persistence.utils import get_engine
from .persistence.montadora_repository import MontadoraRepository
from .view_models import InputMontadora

# O que é fastapi.Form?

# O que é fastapi.RedirectResponse?

# Instanciando o FastAPI
app = FastAPI()
app.mount('/static', StaticFiles(directory='patrocarsweb/static'), name='static')
templates = Jinja2Templates(directory='templates')

# Montadora
SQLModel.metadata.create_all(get_engine())
montadora_repository = MontadoraRepository()

# Rota para Listar Montadoras
@app.get('/montadoras_list')
def montadoras_list(request: Request):
    montadoras = montadora_repository.get_all()
    return templates.TemplateResponse(
        request=request,
        name='montadoras_list.html',
        context={'montadoras': montadoras}
    )

# Rota para Formulário de Montadora
@app.get('/montadoras_form')
def montadoras_form(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='montadoras_form.html'
    )

class MontadoraForm(BaseModel):
    name: str

# Rota para Salvar Montadora
@app.post('/montadora_save')
def montadora_save(request: Request, input: Annotated[InputMontadora, Form()]):
    montadora = Montadora(name=input.name, country=input.country, foundation_year=input.foundation_year)
    montadora_repository.save(montadora)
    return RedirectResponse('/montadoras_list', status_code=303)