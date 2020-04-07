
CREATE TABLE IF NOT EXISTS Patient (
  P_ID INTEGER PRIMARY KEY AUTOINCREMENT,
  Doc_ID INTEGER NOT NULL,
  Appointment_ID INTEGER,
  P_name TEXT,
  DOB DATE NOT NULL,
  Gender TEXT,
  P_number INTEGER,
  P_address TEXT
  PRIMARY KEY(P_ID, Doc_ID)
);

CREATE TABLE IF NOT EXISTS Doctor (
  Doc_ID INTEGER PRIMARY KEY AUTOINCREMENT,
  P_ID INTEGER NOT NULL,
  Doc_name TEXT,
  Doc_number INTEGER
  PRIMARY KEY(Doc_ID, P_ID)
);

CREATE TABLE IF NOT EXISTS Nurse (
  N_ID INTEGER PRIMARY KEY AUTOINCREMENT,
  Doc_ID INTEGER NOT NULL,
  N_name TEXT,
  N_number INTEGER,
  PRIMARY KEY(N_ID, Doc_ID)
);

CREATE TABLE IF NOT EXISTS Appointments (
  Appointment_ID INTEGER PRIMARY KEY AUTOINCREMENT,
  Doc_ID INTEGER NOT NULL,
  Appointment_date DATE NOT NULL,
  Appointment_time TEXT,
  Appointment_type TEXT,
  room_number INTEGER,
  PRIMARY KEY(Appointment_ID, Doc_ID)
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
