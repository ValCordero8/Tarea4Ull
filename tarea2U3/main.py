from fastapi import FastAPI, HTTPException, status
from database import create_db_and_tables, SessionDep
from models import MoviesModel
from random import randint
from sqlmodel import select
from schemas import MovieSchema

app = FastAPI()

create_db_and_tables()

@app.post("/movies")
async def create_movie(movie_data: MovieSchema, database: SessionDep):
    movie = MoviesModel(name=movie_data.name, ano_estreno=movie_data.ano_estreno, duracion=movie_data.duracion, director=movie_data.director, clasificacion=movie_data.clasificacion, genero=movie_data.genero)

    database.add(movie)
    database.commit()
    database.refresh(movie)
    return movie

@app.get("/movies")
async def get_movies(database: SessionDep):
    statement = select(MoviesModel)
    results = database.exec(statement)
    items = results.all()
    return items

@app.get("/movies/{movie_id}")
async def get_movies_by_id(movie_id: int, database: SessionDep):
    movie = database.get(MoviesModel, movie_id)
    
    if not movie: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Peli no encontrada")
    
    return movie