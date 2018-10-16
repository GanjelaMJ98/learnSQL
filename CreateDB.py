import sqlite3
conn = sqlite3.connect('PhoneBook.sqlite')
cursor = conn.cursor()


cursor.execute("""CREATE TABLE `name_t` (
	`name_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL
) """)

cursor.execute("""CREATE TABLE `surname_t` (
	`surname_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`surname`	TEXT NOT NULL
) """)

cursor.execute("""CREATE TABLE `patron_t` (
	`patron_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`patron`	TEXT NOT NULL
)""")

cursor.execute("""CREATE TABLE `street_t` (
	`street_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`street`	TEXT NOT NULL
)""")

cursor.execute("""CREATE TABLE `main` (
	`main_id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`surname_id`	INTEGER,
	`name_id`	INTEGER,
	`patron_id`	INTEGER,
	`street_id`	INTEGER,
	`bild`	INTEGER,
	`block`	INTEGER,
	`appr`	INTEGER,
	`number`	TEXT,
	FOREIGN KEY(`street_id`) REFERENCES `street_t`(`street_id`),
	FOREIGN KEY(`name_id`) REFERENCES `name_t`(`name_id`),
	FOREIGN KEY(`surname_id`) REFERENCES `surname_t`(`surname_id`),
	FOREIGN KEY(`patron_id`) REFERENCES `patron_t`(`patron_id`)
)""")

conn.close()