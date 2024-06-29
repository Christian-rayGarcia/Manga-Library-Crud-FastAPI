CREATE DATABASE mangalibrarydb;

CREATE TABLE Manga(
    bookid int GENERATED ALWAYS AS IDENTITY PRIMARY KEY
    ,title varchar
    ,mangaka varchar
    ,thumbnail varchar
    ,state int
    ,rating int NULL
);
