import psycopg2
from pydantic import BaseModel
from typing import List
import uvicorn
from fastapi import FastAPI, status

app = FastAPI(debug=True)


class Manga(BaseModel):
	id: int = None
	title: str
	mangaka: str = None
	thumbnail: str = None
	state: int
	rating: int = None


@app.get("/status")
async def get_status():
	return "Hello World!"


@app.get("/manga", response_model=List[Manga], status_code=status.HTTP_200_OK)
async def get_mangas():
	# connect to our db
	conn = psycopg2.connect(database="mangalibrarydb", user="", password="")
	cur = conn.cursor()
	cur.execute("SELECT * FROM manga ORDER BY bookid DESC")
	mangas = cur.fetchall()

	formatted_manga = []
	for manga in mangas:
		formatted_manga.append(Manga(
			id=manga[0], title=manga[1], mangaka=manga[2], thumbnail=manga[3], state=manga[4], rating=manga[5]))

	cur.close()
	conn.close()

	return formatted_manga


@app.post("/manga", status_code=status.HTTP_201_CREATED)
async def new_manga(manga: Manga):
	conn = psycopg2.connect(database="mangalibrarydb", user="christian-raygarcia", password="")
	cur = conn.cursor()
	cur.execute(f"INSERT INTO manga (title, mangaka, thumbnail, state) VALUES ('{manga.title}', '{manga.mangaka}', '{manga.thumbnail}', '{manga.state}')")

	cur.close()
	conn.commit()
	conn.close()


if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)
