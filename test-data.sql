INSERT INTO Patient
  (Doc_ID, P_name, DOB, Gender, P_number, P_address, Appointment_ID)
VALUES
  (1, 'John Atkinson', '1967-02-01', 'Male', 2022340258, '1000 enterprise way, NY 30980', 1),
  (2, 'James Sweeney', '1969-12-30', 'Male', 2022340260, '420 Safeway blvd, DC 20001', 2),
  (3, 'Janie Fuentes', '1967-02-11', 'Female', 6462340258, '3636 stone court, AZ 20234', 3),
  (4, 'Toni Russo', '1997-10-10', 'Male', 6462340264, '43 moon town, DC 20001', 4),
  (5, 'Ray Mueller', '1967-02-21', 'Male', 7402340258, 'Jackson street, CA 99441', 5),
  (6, 'Kate Golden', '2000-02-03', 'Female', 7402340268, '439 success road, TX 20059', 6),
  (7, 'Doe Spade', '1997-11-09', 'Male', 2022340000, '1002 planet earth, CA 99441', 7),
  (8, 'Amber Adams', '1996-08-23', 'Female', 6462340272, '1020 enterprise way, NY. 30980', 8),
  (9, 'Rose Mcneil', '1993-09-09', 'Female', 7402340000, '92 cone lane, AZ. 20234', 9),
  (10, 'Nicki Bee', '2002-04-01', 'Female', 8002340825, '50 shirt blvd, TX. 20059', 10);

INSERT INTO Doctor
  (P_ID, Doc_name, Doc_number)
VALUES
  (1, 'Dr. Morris Armstrong', 9196061032),
  (2, 'Dr. Latifa Brown', 2394306448),
  (3, 'Dr. Chad Jackson', 4153290460),
  (4, 'Dr. Cooper Ross', 8106825332),
  (5, 'Dr. Daniel Manning', 2603658655),
  (6, 'Dr. Bolu Brock', 5703809578),
  (7, 'Dr. Paul Garza', 3139350949),
  (8, 'Dr. Kate Taylor', 5173346436),
  (9, 'Dr. Betty Martin', 8434071526),
  (10, 'Dr. Dora Garza', 4048924190);

INSERT INTO Nurse
  (Doc_ ID, N_name, N_number)
VALUES
  (1, 'Sian Sanchez', 2026061032),
  (2, 'Tre Beasley', 2300006448),
  (3, 'Keira Whitaker', 4132590460),
  (4, 'Usamah Bouvet', 2026825332),
  (5, 'Daniel Manning', 6403658644),
  (6, 'Tayyab Barton', 5703800038),
  (7, 'Silas Parks', 3139312349),
  (8, 'Lila Parrish', 6469046436),
  (9, 'Finbar Roche', 8004077726),
  (10, 'Darcie Connolly', 2024924190);

INSERT INTO Appointments
  (Doc_ID, Appointment_date, Appointment_time, Appointment_type, room_number)
VALUES
  (1, '2020-04-20', '5PM', 'Checkup', 420),
  (2, '2020-05-01', '2:30PM', 'Dental', 240),
  (3, '2020-05-14', '3PM', 'Vaccine Shot', 300),
  (4, '2020-04-21', '2PM', 'COVID-19 Test', 560),
  (5, '2020-04-22', '9AM', 'Surgery', 100),
  (6, '2020-04-27', '11AM', 'Checkup', 426),
  (7, '2020-06-01', '4:30PM', 'Checkup', 220),
  (8, '2020-06-02', '8AM', 'COVID-19 Test', 560),
  (9, '2020-05-05', '10AM', 'Flu Shot', 220),
  (10, '2020-05-08', '4PM', 'Checkup', 147);

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

