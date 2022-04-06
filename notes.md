


inside database:




DROP TABLE IF EXISTS users;
CREATE TABLE users (
    user_id serial PRIMARY KEY,
    username varchar(100),
    email varchar(100),
    password_digest varchar(1000),
    rank int,
    admin boolean
);

INSERT INTO users (username, email, password_digest, rank, admin) VALUES ('test', 'test@test.com', 'test', 4, True);

INSERT INTO users (username, email, password_digest, rank, admin) VALUES ('test1', 'test1@test.com', 'test1', 5, True);


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
















DROP TABLE IF EXISTS users;
CREATE TABLE users (
    user_id serial PRIMARY KEY,
    username varchar(100),
    email varchar(100),
    password_digest varchar(100),
    rank int,
    admin boolean
);

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
