
CREATE TABLE IF NOT EXISTS Patient (
  pid INTEGER PRIMARY KEY AUTOINCREMENT,
  did INTEGER NOT NULL,
  aid INTEGER,
  P_name TEXT,
  DOB DATE NOT NULL,
  Gender TEXT,
  P_number INTEGER,
  P_address TEXT
);

CREATE TABLE IF NOT EXISTS Doctor (
  did INTEGER PRIMARY KEY AUTOINCREMENT,
  pid INTEGER NOT NULL,
  Doc_name TEXT,
  Doc_number INTEGER
);

CREATE TABLE IF NOT EXISTS Nurse (
  nid INTEGER PRIMARY KEY AUTOINCREMENT,
  did INTEGER NOT NULL,
  N_name TEXT,
  N_number INTEGER
);

CREATE TABLE IF NOT EXISTS Appointments (
  aid INTEGER PRIMARY KEY AUTOINCREMENT,
  did INTEGER NOT NULL,
  Appointment_date DATE NOT NULL,
  Appointment_time TEXT,
  Appointment_type TEXT,
  room_number INTEGER
);



-- CREATE TABLE IF NOT EXISTS Sailors (
--   sid INTEGER PRIMARY KEY AUTOINCREMENT,
--   name TEXT,
--   age INTEGER,
--   experience INTEGER -- years of experience
-- );

-- CREATE TABLE IF NOT EXISTS Boats (
--   bid INTEGER PRIMARY KEY AUTOINCREMENT,
--   name TEXT,
--   color TEXT
-- );

-- CREATE TABLE IF NOT EXISTS Voyages (
--   sid INTEGER NOT NULL,
--   bid INTEGER NOT NULL,
--   date_of_voyage DATE NOT NULL,
--   PRIMARY KEY(sid, bid, date_of_voyage)
-- );
