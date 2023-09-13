CREATE DATABASE chat-app-db;
use chat-app-db;

CREATE TABLE rooms (
    ID int NOT NULL AUTO_INCREMENT,
    name verchar(255) NOT NULL,
    PRIMARY KEY (ID)
)

CREATE TABLE users (
    ID int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    PRIMARY KEY (ID)
)

CREATE TABLE messages (
    ID int NOT NULL AUTO_INCREMENT,
    user_id int NOT NULL,
    room_id int NOT NULL,
    msg varchar(255) NOT NULL,
    PRIMARY KEY (ID),
    user_id FOREIGN KEY REFERENCE users(ID),
    room_id FOREIGN KEY REFERENCE rooms(ID)
)
