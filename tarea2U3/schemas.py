from pydantic import BaseModel

class MovieSchema(BaseModel):
    name: str
    ano_estreno: str
    duracion: str
    director: str
    clasificacion: str
    genero: str