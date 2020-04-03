CREATE TABLE IF NOT EXISTS Sailors (
  sid INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  age INTEGER,
  experience INTEGER -- years of experience
);

CREATE TABLE IF NOT EXISTS Boats (
  bid INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  color TEXT
);

CREATE TABLE IF NOT EXISTS Voyages (
  sid INTEGER NOT NULL,
  bid INTEGER NOT NULL,
  date_of_voyage DATE NOT NULL,
  PRIMARY KEY(sid, bid, date_of_voyage)
);
