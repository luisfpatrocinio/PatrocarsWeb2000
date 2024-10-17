from sqlmodel import Session, select
from .utils import get_engine
from patrocarsweb.models import Montadora
# TODO: Conferir importação relativa.

class MontadoraRepository():
    def __init__(self) -> None:
        self.session = Session(get_engine())

    def get_all(self):
        _statement = select(Montadora)
        montadoras = self.session.exec(_statement).all()
        return montadoras
    
    def save(self, montadora: Montadora):
        self.session.add(montadora)
        self.session.commit()
        self.session.refresh(montadora)
        return montadora