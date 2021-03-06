CREATE TABLE IF NOT EXISTS Patient (
  pid INTEGER PRIMARY KEY AUTOINCREMENT,
  P_name TEXT,
  medical_history TEXT,
  DOB DATE NOT NULL,
  Gender TEXT,
  P_number INTEGER,
  P_address TEXT
);

CREATE TABLE IF NOT EXISTS Doctor (
  did INTEGER PRIMARY KEY AUTOINCREMENT,
  Doc_name TEXT,
  Doc_number INTEGER,
  Doc_email TEXT,
  Doc_password TEXT
);

CREATE TABLE IF NOT EXISTS Nurse (
  nid INTEGER PRIMARY KEY AUTOINCREMENT,
  N_name TEXT,
  N_number INTEGER
);

CREATE TABLE IF NOT EXISTS Appointments (
  aid INTEGER PRIMARY KEY AUTOINCREMENT,
  did INTEGER NOT NULL,
  nid INTEGER NOT NULL,
  pid INTEGER NOT NULL,
  Appointment_date DATE NOT NULL,
  Appointment_time TEXT,
  Appointment_type TEXT,
  room_number INTEGER
);