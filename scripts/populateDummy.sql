INSERT INTO members
(first_name,last_name,email) VALUES
('Jim', 'Bo', 'Jimbo@hotmail.ca'),
('Sarah','Connor','sarahCon@outlook.com'),
('Tiff','Hadish','tiffy@gmail.com'),
('Selena','Gomez','Selena@gmail.com'),
('Rue','Euphoria','rue@gmail.com'),
('Jonny','Shoes','jon@gmail.com'),
('Andrew','Biggums','drewy@gmail.com'),
('Justin','Pookie','justin@gmail.com'),
('Nabil','Boss','nabil@gmail.com')
ON CONFLICT DO NOTHING;

-- INSERT INTO goals
-- (member_id,weight,time,streak) VALUES
-- (1,175,6,12),
-- (2,220,6,12),
-- (3,150,6,12)
-- ON CONFLICT DO NOTHING;

INSERT INTO trainers 
(first_name,last_name,email,salary) VALUES
('John', 'Doe', 'john.doe@example.com', 75000),
('Jane', 'Smith', 'jane.smith@example.com', 37500),
('Jim', 'Beam', 'jim.beam@example.com', 60000)
ON CONFLICT DO NOTHING;

-- INSERT INTO availabilities
-- (trainer_id,day,start_time,end_time) VALUES
-- (1,'2024-05-01','11:00:00','12:00:00'),
-- (1,'2024-05-01','12:30:00','13:30:00'),
-- (1,'2024-05-01','14:00:00','15:00:00'),
-- (2,'2024-05-01','11:00:00','12:00:00'),
-- (2,'2024-05-01','12:30:00','13:30:00'),
-- (2,'2024-05-01','14:00:00','15:00:00'),
-- (3,'2024-05-01','11:00:00','12:00:00'),
-- (3,'2024-05-01','12:30:00','13:30:00'),
-- (3,'2024-05-01','14:00:00','15:00:00')
-- ON CONFLICT DO NOTHING;

INSERT INTO admins
(email,salary,position,last_name,first_name) VALUES 
('J@gmail.com',250000,'HR','Smith','John'),
('A@gmail.com',300000,'CEO','Smith','June'),
('B@gmail.com',275000,'CFO','Smith','Bob')
ON CONFLICT DO NOTHING;

INSERT INTO rooms
(room_number,name,status) VALUES
(101,'Party',False),
(102,'Party_2',False),
(103,'Party_3',False)
ON CONFLICT DO NOTHING;

INSERT INTO Equipment
(name,status) VALUES
('10LB Dumbell',True),
('10LB Dumbell',True),
('25LB Dumbell',True),
('25LB Dumbell',True),
('50LB Dumbell',True),
('50LB Dumbell',False)
ON CONFLICT DO NOTHING;
