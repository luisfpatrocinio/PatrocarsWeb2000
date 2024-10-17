from sqlmodel import SQLModel, Field

class Montadora(SQLModel, table=True):
  id: int | None = Field(default=None, primary_key=True)
  name: str
  country: str
  foundation_year: int