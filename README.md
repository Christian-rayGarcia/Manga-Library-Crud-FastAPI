**Manga CRUD Library with FASTAPI**

This project is a simple CRUD library built with FASTAPI, connected to a local PostgreSQL server. It provides the ability to manage manga records in a PostgreSQL database. The database includes the following tables and fields:

Table: Manga
- bookeid: A boolean indicating if the manga is booked.
- title: The title of the manga.
- mangaka (author): The author of the manga.
- thumbnail: A link or path to the manga's thumbnail image.
- state: An integer representing the reading status (1 = wishlist, 2 = reading, 3 = read).
- rating: The rating of the manga.

**Features**

- GET: Retrieve manga records.
- POST: Add new manga records.
- PUT: Updating State, Updating Rating.
- DELETE: Remove manga records.

![Screenshot 2024-06-29 at 16 43 48](https://github.com/Christian-rayGarcia/Manga-Library-Crud-FastAPI/assets/47110238/740f0279-ea3b-4b98-932c-0f53d4b429b5)

![Screenshot 2024-06-29 at 16 34 33](https://github.com/Christian-rayGarcia/Manga-Library-Crud-FastAPI/assets/47110238/2a5d019c-03b5-4b9f-801e-e53db7e49d87)
