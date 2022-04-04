



inside database:

DROP TABLE IF EXISTS users;
CREATE TABLE users (
    user_id serial PRIMARY KEY,
    username varchar(100),
    email varchar(100),
    password_digest varchar(100),
    rank int
);

INSERT INTO users (username, email, password_digest, rank) VALUES ('test', 'test@test.com', 'test', 4);

INSERT INTO users (username, email, password_digest, rank) VALUES ('test1', 'test1@test.com', 'test1', 5);







DROP TABLE IF EXISTS admin;
CREATE TABLE admin (
    admin_id serial PRIMARY KEY,
    username varchar(100),
    email varchar(100),
    password_digest varchar(100)
);

INSERT INTO admin (username, email, password_digest) VALUES ('boss', 'boss@test.com', 'boss');




DROP TABLE IF EXISTS lobby;
CREATE TABLE lobby (
    lobby_id serial PRIMARY KEY,
    player_1_key INT,
    FOREIGN KEY(player_1_key)
    REFERENCES users(user_id),
    player_2_key INT,
    FOREIGN KEY(player_2_key)
    REFERENCES users(user_id),
    history varchar(50000)
);

INSERT INTO lobby (player_1_key, player_2_key, history) VALUES (1, 2, 'history');







DROP TABLE IF EXISTS chat;
CREATE TABLE chat (
    message_id serial PRIMARY KEY,
    lobby_id INT,
    FOREIGN KEY(lobby_id)
    REFERENCES lobby(lobby_id),
    user_id INT,
    FOREIGN KEY(user_id)
    REFERENCES users(user_id),
    message varchar(500),
    time date
);

INSERT INTO chat (lobby_id, user_id, message, time) VALUES (1, 1, 'hello', '2022-04-04');




inside the .env file:

DATABASE_URL=postgres://yaegrrmpgbwrti:ec575d01211bf2d06c70954781406007730dd6efc093eecb12972f44c9c530f7@ec2-99-80-170-190.eu-west-1.compute.amazonaws.com:5432/dcqpm3ubt7k4mk
SECRET_KEY=gg
