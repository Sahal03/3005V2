
INSERT INTO members (first_name, last_name, email)
VALUES 
    ('Dragon', 'Doe', 'dragon.doe@example.com'),
    ('Arnold', 'Smith', 'arnold.smith@example.com'),
    ('Michael', 'Jackson', 'michael.jackson@example.com'),
    ('Alice', 'Potter', 'alice.potter@example.com'),
    ('Harry', 'Potter', 'harry.potter@example.com'),
    ('yasuo', 'legend', 'yasuo.legend@example.com');


INSERT INTO goals (member_id, weight, time, streak)
VALUES 
    (1, 176.5, 69, 13),
    (2, 78.2, 78, 19),
    (3, 180.0, 120, 200),
    (4, 68.0, 123, 534),
    (5, 92.5, 76, 86),
    (6, 73.8, 456, 180);


INSERT INTO health (member_id, average_bpm, muscle_mass, weight, bmi)
VALUES 
    (1, 75.5, 76.2, 70.5, 23.5),
    (2, 84.5, 98.5, 65.2, 22.2),
    (3, 103.2, 63.0, 88.0, 25.7),
    (4, 123.0, 56.0, 73.0, 27.2),
    (5, 154.0, 59.0, 54.5, 21.9),
    (6, 72.0, 69.0, 87.0, 23.9);


INSERT INTO exercise_routines (name, duration, type, defecit)
VALUES 
    ('Running', 250.0, 'Cardio', 2000),
    ('Leg Press 200 LB', 45.0, 'Legs', 500),
    ('Yoga', 95.3, 'Flexibility', 50),
    ('Cycling', 120.5, 'Cardio', 800),
    ('Push-ups', 35.4, 'Push', 100),
    ('Plank', 45.0, 'Pull', 400);


INSERT INTO fitness_achievement (name, type)
VALUES 
    ('Marathon Finisher', 'Cardio'),
    ('Deadlift Champion', 'Legs'),
    ('Yoga Enjoyer', 'Flexibility'),
    ('Cycling Champion', 'Cardio'),
    ('Bench Press Champion', 'Push'),
    ('Its Too Easy (Pull Ups)', 'Pull');


INSERT INTO health_statistics (name, calories_burned, minutes_ran, weight_carried)
VALUES 
    ('Daily Workout', 535.0, 31.2, 137.5),
    ('Weekly Brawl', 1524.0, 127.0, 355.0),
    ('Monthly Feast Challenge', 3050.0, 248.0, 625.0),
    ('Weekly Run', 2304.5, 167.2, 230.5),
    ('Ninja Workout', 802.0, 61.0, 153.0),
    ('Monthly Beep Test', 3501.0, 324.0, 423.0);


INSERT INTO trainers (first_name, last_name, email, salary)
VALUES 
    ('Emily', 'Blue', 'emily.blue@example.com', 50000.0),
    ('David', 'Wonka', 'david.wonka@example.com', 55000.0),
    ('Oragami', 'Jones', 'oragami.jones@example.com', 60000.0),
    ('Bilbo', 'Baggins', 'bilbo.baggins@example.com', 52000.0),
    ('Daniel', 'Voldemort', 'daniel.voldemort@example.com', 58000.0),
    ('Taylor', 'Taylor', 'taylor.taylor@example.com', 62000.0);


INSERT INTO availabilities (trainer_id, day, start_time, end_time, available)
VALUES 
    (1, '2024-04-3', '09:00:00', '11:00:00', TRUE),
    (2, '2024-04-21', '11:00:00', '12:00:00', TRUE),
    (3, '2024-04-7', '12:00:00', '13:00:00', FALSE),
    (4, '2024-04-13', '08:00:00', '10:00:00', TRUE),
    (5, '2024-04-12', '07:00:00', '11:00:00', TRUE),
    (6, '2024-04-17', '10:00:00', '12:00:00', FALSE);    


INSERT INTO admins (email, salary, position, first_name, last_name)
VALUES 
    ('admin1@example.com', 180000.0, 'Manager', 'Admin', 'One'),
    ('admin2@example.com', 95000.0, 'Supervisor', 'Admin', 'Two'),
    ('admin3@example.com', 50000.0, 'Employee', 'Admin', 'Three'),
    ('admin4@example.com', 192000.0, 'Manager', 'Admin', 'Four'),
    ('admin5@example.com', 88000.0, 'Employee', 'Admin', 'Five'),
    ('admin6@example.com', 72000.0, 'Employee', 'Admin', 'Six');


INSERT INTO rooms (room_number, name, status)
VALUES 
    (101, 'Cardio Room', TRUE),
    (102, 'Upstairs', TRUE),
    (103, 'Yoga Room', FALSE),
    (104, 'Swimming Pool', TRUE),
    (105, 'Sauna Room', TRUE),
    (106, 'Cycle Room', FALSE);


INSERT INTO classes (instructor, quantity, capacity, class_name, isFull)
VALUES 
    ('Brown Brown', 10, 20, 'Cardio Blast', FALSE),
    ('Willy Wilson', 15, 25, 'Strength Training', FALSE),
    ('David Jones', 15, 15, 'Yoga Flow', TRUE),
    ('Sofia Paper', 12, 20, 'Swimming Lessons', FALSE),
    ('Danielle Daniels', 18, 25, 'Spinning Challenge', FALSE),
    ('Example Example', 10, 15, 'Mindfulness Meditation', FALSE);


INSERT INTO Equipment (name, status)
VALUES 
    ('Treadmill', TRUE),
    ('Dumbbells', TRUE),
    ('Abs Machine', FALSE),
    ('Bench Press', TRUE),
    ('Leg Press', TRUE),
    ('Pull Up Assist', FALSE);

