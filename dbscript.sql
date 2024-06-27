CREATE DATABASE mangalibrarydb;

CREATE TABLE Manga(
    bookid serial primary key
    ,title CHARACTER VARYING NULL
    ,mangaka CHARACTER VARYING NULL
    ,thumbnail CHARACTER VARYING NULL
    ,state int
    ,rating int NULL
);
