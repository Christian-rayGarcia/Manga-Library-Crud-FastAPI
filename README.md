**Manga CRUD Library with FASTAPI**

This project is a simple CRUD library built with FASTAPI, connected to a local PostgreSQL server. It provides the ability to manage manga records in a PostgreSQL database. The database includes the following tables and fields:

Table: Manga
- bookeid: A boolean indicating if the manga is booked.
- title: The title of the manga.
- mangaka (author): The author of the manga.
- thumbnail: A link or path to the manga's thumbnail image.
- state: An integer representing the reading status (1 = read, 2 = reading, 3 = wishlist).
- rating: The rating of the manga.

**Features**

- GET: Retrieve manga records.
- POST: Add new manga records.
- PUT: Update existing manga records.
- DELETE: Remove manga records.

![Screenshot 2024-06-29 at 16 31 54](https://github.com/Christian-rayGarcia/Manga-Library-Crud-FastAPI/assets/47110238/455b4d66-706c-418c-9c94-68c989ec82b7)
![Screenshot 2024-06-27 at 17 16 33](https://github.com/Christian-rayGarcia/Manga-Library-Crud-FastAPI/assets/47110238/3e64845a-302c-46a5-b693-6c41f3eb0b11)
