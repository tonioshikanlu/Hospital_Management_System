
INSERT INTO Sailors
  (name, age, experience)
VALUES
  ('john', 32, 5),
  ('jane', 22, 3),
  ('janie', 45, 17);

INSERT INTO Boats
  (name, color)
VALUES
  ('Water Bug', 'blue'),
  ('Sundance', 'green'),
  ('Moonrise', 'red');

INSERT INTO Voyages
  (sid, bid, date_of_voyage)
VALUES
  (1, 1, '2020-02-01'),
  (1, 2, '2020-02-02'),
  (1, 3, '2020-02-03'),
  (2, 1, '2020-02-02'),
  (2, 1, '2020-02-03'),
  (3, 3, '2020-02-01');
