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

![Screenshot 2024-06-29 at 16.31.54.png](..%2F..%2F..%2FDesktop%2FScreenshot%202024-06-29%20at%2016.31.54.png)![Screenshot 2024-06-29 at 16.32.18.png](..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fvr%2Fndsqrdqx2mx9n7sqdfspnnx00000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_TZ6QXo%2FScreenshot%202024-06-29%20at%2016.32.18.png)