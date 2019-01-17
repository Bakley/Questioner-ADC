create_tbl_users = """CREATE TABLE IF NOT EXISTS user(
    userid serial PRIMARY KEY,
    firstname VARCHAR (50) NOT NULL,
    lastname VARCHAR (50) NOT NULL,
    othername VARCHAR (50) NOT NULL,
    username VARCHAR (50) UNIQUE NOT NULL,
    userpassword VARCHAR (50) NOT NULL,
    email VARCHAR (355) UNIQUE NOT NULL,
    phonenumber INTEGER NOT NULL,
    registered TIMESTAMP DEFAULT NOW(),
    last_login TIMESTAMP,
    isAdmin BOOLEAN DEFAULT FALSE
);"""

create_tbl_meetups = """CREATE TABLE IF NOT EXISTS meetups(
    meetupid serial PRIMARY KEY,
    user_key_id INTEGER,
    location VARCHAR (50) NOT NULL,
    topic VARCHAR (50) NOT NULL,
    tags TEXT []NOT NULL,
    images TEXT [],
    createdOn TIMESTAMP NOT NULL,
    happeningOn TIMESTAMP NOT NULL, 
    FOREIGN KEY (user_key_id) REFERENCES users (user_id) ON DELETE CASCADE
);"""

create_tbl_questions = """CREATE TABLE IF NOT EXISTS questions(
    questionid serial PRIMARY KEY,
    created_by_id INTEGER,
    meetup_on_id INTEGER,
    title VARCHAR (50) NOT NULL,
    body VARCHAR (100) NOT NULL,
    votes INTEGER NOT NULL,
    createdOn TIMESTAMP NOT NULL,
    FOREIGN KEY (meetup_on_id) REFERENCES meetups (meetup_id) ON DELETE CASCADE,
    FOREIGN KEY (created_by_id) REFERENCES users (user_id) ON DELETE CASCADE
);
"""

query_insert_admin = """INSERT INTO user (firstname, lastname, username, userpassword, email, phonenumber, isAdmin)
VALUES ('superuser', 'superadmin', 'Admin', 'Admin@254', 'super@admin.org', '0703912965', 'TRUE');"""