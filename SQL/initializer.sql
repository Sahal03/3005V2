DROP TABLE goals;
DROP TABLE health;
DROP TABLE members;
DROP TABLE availabilities;
DROP TABLE trainers;
DROP TABLE rooms;
DROP TABLE admins;
DROP TABLE classes;
DROP TABLE equipments;
DROP TABLE exercise_routines;
DROP TABLE fitness_achievement;
DROP TABLE health_statistics;

create table if not exists members 
    (
        member_id SERIAL,
        first_name varchar(255) not null,
        last_name varchar(255) not null,
        email varchar(255) not null unique,
        primary key(member_id)
    );

create table if not exists goals
    (
       member_id int, 
       weight FLOAT,
       time int,
       streak int ,
       foreign key(member_id) references members
    );

create table if not exists health
    (
       member_id int, 
       average_bpm FLOAT,
       muscle_mass FLOAT,
       weight FLOAT,
       bmi FLOAT,
       foreign key(member_id) references members
    );

create table if not exists exercise_routines
(
    exercise_id SERIAL,
    name varchar(55),
    duration FLOAT,
    type varchar(15),
    defecit int,
    primary key(exercise_id)

);

create table if not exists fitness_achievement
(
    fitness_id SERIAL,
    name varchar(55),
    type varchar(15), 
    primary key(fitness_id)

);

create table if not exists health_statistics
(
    stat_id SERIAL,
    name varchar(55),
    calories_burned FLOAT,
    minutes_ran FLOAT,
    weight_carried FLOAT,
    primary key(stat_id)

);

create table if not exists trainers
    (
        trainer_id SERIAL,
        first_name varchar(255) not null,
        last_name varchar(255) not null,
        email varchar(255) not null unique,
        salary FLOAT,
        primary key(trainer_id)
    );

create table if not exists availabilities
    (
        trainer_id int,
        day DATE not null,
        start_time TIME not null,
        end_time TIME not null,
        available boolean,
        foreign key(trainer_id) references trainers
    );

create table if not exists admins
    (
        admin_id SERIAL,
        email varchar(255) not null unique,
        salary FLOAT,
        position varchar(255),
        last_name varchar(255) not null,
        first_name varchar(255) not null,
        primary key(admin_id)
    );

create table if not exists rooms
    (
        room_number int not null unique,
        name varchar(255),
        status boolean,
        primary key(room_number)
    );



create table if not exists classes 
    (
        class_id SERIAL,
        instructor varchar(255) not null,
        quantity int,
        capacity int,
        class_name varchar(255) not null,
        isFull boolean,
        primary key(class_id)
    );

create table if not exists equipments
    (
        equipment_id SERIAL,
        name varchar(255) not null,
        status boolean
    );