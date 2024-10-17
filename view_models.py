from pydantic import BaseModel

class InputMontadora(BaseModel):
    name: str
    country: str
    foundation_year: int