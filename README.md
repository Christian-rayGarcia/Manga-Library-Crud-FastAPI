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
