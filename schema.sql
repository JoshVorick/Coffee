DROP TABLE users;
DROP TABLE events;

CREATE TABLE users (
    name varchar(255) NOT NULL,
    profileid varchar(255) NOT NULL,
    accessid varchar(255) NOT NULL,
    accessid varchar(255) NOT NULL,
    PRIMARY KEY(profileid)
);

CREATE TABLE events (
    id SERIAL NOT NULL,
    user1 varchar(255) NOT NULL,
    user2 varchar(255) NOT NULL,
    location varchar(255) NOT NULL,
    time timestamp,
    type varchar(255) NOT NULL,
    status varchar(255) NOT NULL,
    PRIMARY KEY(id)
);
