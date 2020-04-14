INSERT INTO Patient
  (P_name, DOB, Gender, P_number, P_address, medical_history)
VALUES
  ('John Atkinson', '1967-02-01', 'Male', 2022340258, '1000 enterprise way, NY 30980', 'Asthmatic'),
  ('James Sweeney', '1969-12-30', 'Male', 2022340260, '420 Safeway blvd, DC 20001', 'Bone Disease'),
  ('Janie Fuentes', '1967-02-11', 'Female', 6462340258, '3636 stone court, AZ 20234', 'Depression'),
  ('Toni Russo', '1997-10-10', 'Male', 6462340264, '43 moon town, DC 20001', 'Heart Attack'),
  ('Ray Mueller', '1967-02-21', 'Male', 7402340258, 'Jackson street, CA 99441', 'Stomach Ulcer'),
  ('Kate Golden', '2000-02-03', 'Female', 7402340268, '439 success road, TX 20059', 'Diabetes Type II'),
  ('Doe Spade', '1997-11-09', 'Male', 2022340000, '1002 planet earth, CA 99441', 'Mental Illness'),
  ('Amber Adams', '1996-08-23', 'Female', 6462340272, '1020 enterprise way, NY. 30980', 'Breast Cancer'),
  ('Rose Mcneil', '1993-09-09', 'Female', 7402340000, '92 cone lane, AZ. 20234', 'Migraines'),
  ('Nicki Bee', '2002-04-01', 'Female', 8002340825, '50 shirt blvd, TX. 20059', 'Asthmatic');

INSERT INTO Doctor
  (Doc_name, Doc_number, Doc_email, Doc_password)
VALUES
  ('Dr. Morris Strong', 9196061032, 'strong@aol.com', 'pass10'),
  ('Dr. Latifa Brown', 2394306448, 'brown@aol.com', 'pass11'),
  ('Dr. Chad Jackson', 4153290460, 'chad@aol.com', 'pass12'),
  ('Dr. Cooper Ross', 8106825332, 'rossg@aol.com', 'pass13'),
  ('Dr. Daniel Mang', 2603658655, 'mang@aol.com', 'pass14'),
  ('Dr. Bolu Brock', 5703809578, 'bolu@aol.com', 'pass15'),
  ('Dr. Paul Garza', 3139350949, 'paul@aol.com', 'pass16'),
  ('Dr. Kate Taylor', 5173346436, 'kate@aol.com', 'pass17'),
  ('Dr. Betty Martin', 8434071526, 'betty@aol.com', 'pass18'),
  ('Dr. Dora Garza', 4048924190, 'dora@aol.com', 'pass19');

INSERT INTO Nurse
  (N_name, N_number)
VALUES
  ('Sian Sanchez', 2026061032),
  ('Tre Beasley', 2300006448),
  ('Keira Whitaker', 4132590460),
  ('Usamah Bouvet', 2026825332),
  ('Daniel Manning', 6403658644),
  ('Tayyab Barton', 5703800038),
  ('Silas Parks', 3139312349),
  ('Lila Parrish', 6469046436),
  ('Finbar Roche', 8004077726),
  ('Darcie Connolly', 2024924190);

INSERT INTO Appointments
  (did, nid, pid, Appointment_date, Appointment_time, Appointment_type, room_number)
VALUES
  (1, 1, 2, '2020-04-20', '5PM', 'Checkup', 420),
  (2, 3, 5,  '2020-05-01', '2:30PM', 'Dental', 240),
  (3, 7, 3, '2020-05-14', '3PM', 'Vaccine Shot', 300),
  (4, 5, 9, '2020-04-21', '2PM', 'COVID-19 Test', 560),
  (5, 4, 10, '2020-04-22', '9AM', 'Surgery', 100),
  (6, 2, 7, '2020-04-27', '11AM', 'Checkup', 426),
  (7, 10, 6, '2020-06-01', '4:30PM', 'Checkup', 220),
  (8, 8, 1, '2020-06-02', '8AM', 'COVID-19 Test', 560),
  (9, 10, 4, '2020-05-05', '10AM', 'Flu Shot', 220),
  (10, 6, 8, '2020-05-08', '4PM', 'Checkup', 147);

-- INSERT INTO Sailors
--   (name, age, experience)
-- VALUES
--   ('john', 32, 5),
--   ('jane', 22, 3),
--   ('janie', 45, 17);

-- INSERT INTO Boats
--   (name, color)
-- VALUES
--   ('Water Bug', 'blue'),
--   ('Sundance', 'green'),
--   ('Moonrise', 'red');

-- INSERT INTO Voyages
--   (sid, bid, date_of_voyage)
-- VALUES
--   (1, 1, '2020-02-01'),
--   (1, 2, '2020-02-02'),
--   (1, 3, '2020-02-03'),
--   (2, 1, '2020-02-02'),
--   (2, 1, '2020-02-03'),
--   (3, 3, '2020-02-01');

