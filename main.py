import psycopg2
from pydantic import BaseModel
from typing import List
import uvicorn
from fastapi import FastAPI, status

app = FastAPI(debug=True)


class Manga(BaseModel):
	bookid: int = None
	title: str
	mangaka: str = None
	thumbnail: str = None
	state: int
	rating: None


class UpdateRatingRequestBody(BaseModel):
	title: str
	new_rating: int


class UpdateStateRequestBody(BaseModel):
	title: str
	new_state: int

class DeleteBody(BaseModel):
	title: str


@app.get("/status")
async def get_status():
	return "Hello World!"


@app.get("/manga", response_model=List[Manga], status_code=status.HTTP_200_OK)
async def get_mangas():
	# connect to our db
	conn = psycopg2.connect(database="mangalibrarydb", user="", password="testtest123")
	cur = conn.cursor()
	cur.execute("SELECT * FROM manga ORDER BY bookid DESC")
	mangas = cur.fetchall()

	formatted_manga = []
	for manga in mangas:
		formatted_manga.append(Manga(
			bookid=manga[0], title=manga[1], mangaka=manga[2], thumbnail=manga[3], state=manga[4], rating=manga[5]))

	cur.close()
	conn.close()

	return formatted_manga


@app.post("/manga", status_code=status.HTTP_201_CREATED)
async def new_manga(manga: Manga):
	conn = psycopg2.connect(database="mangalibrarydb", user="christian-raygarcia", password="testtest123")
	cur = conn.cursor()
	cur.execute(
		f"INSERT INTO manga (title, mangaka, thumbnail, state) VALUES ('{manga.title}', '{manga.mangaka}', '{manga.thumbnail}', '{manga.state}')")

	cur.close()
	conn.commit()
	conn.close()


@app.put("/manga/updating_rating", status_code=200)
async def update_rating(update_rating_body: UpdateRatingRequestBody):
	conn = psycopg2.connect(database="mangalibrarydb", user="christian-raygarcia", password="testtest123")
	cur = conn.cursor()
	cur.execute(f"UPDATE manga SET rating = {update_rating_body.new_rating} WHERE title = '{update_rating_body.title}'")

	cur.close()
	conn.commit()
	conn.close()
	return


# endpoint to change 1/2/3 if list/started/read
@app.put("/manga/updating_state", status_code=200)
async def update_rating(update_state_body: UpdateStateRequestBody):
	conn = psycopg2.connect(database="mangalibrarydb", user="christian-raygarcia", password="testtest123")
	cur = conn.cursor()
	cur.execute(f"UPDATE manga SET state = {update_state_body.new_state} WHERE title = '{update_state_body.title}'")

	cur.close()
	conn.commit()
	conn.close()
	return


@app.delete("/manga/delete_manga", status_code=status.HTTP_410_GONE)
async def update_rating(delete_record: DeleteBody):
	conn = psycopg2.connect(database="mangalibrarydb", user="christian-raygarcia", password="testtest123")
	cur = conn.cursor()
	cur.execute(f"DELETE FROM manga WHERE title = '{delete_record.title}'")

	cur.close()
	conn.commit()
	conn.close()
	return


if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)
