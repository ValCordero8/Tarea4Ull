from sqlmodel import SQLModel, Field

class MoviesModel(SQLModel, table=True):
    __tablename__ = "Movies"

    id: int = Field(primary_key=True)
    name: str
    ano_estreno: str
    duracion: str
    director: str
    clasificacion: str
    genero: str