DROP TABLE goals;
DROP TABLE members;
DROP TABLE availabilities;
DROP TABLE trainers;
DROP TABLE schedules;
DROP TABLE rooms;
DROP TABLE admins;
DROP TABLE classes;
DROP TABLE Equipment;

create table if not exists members 
    (
        member_id SERIAL,
        first_name varchar(255) not null,
        last_name varchar(255) not null,
        email varchar(255),
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

create table if not exists trainers
    (
        trainer_id SERIAL,
        first_name varchar(255) not null,
        last_name varchar(255) not null,
        email varchar(255),
        salary FLOAT,
        primary key(trainer_id)
    );

create table if not exists availabilities
    (
        trainer_id int,
        day DATE not null,
        start_time TIME not null,
        end_time TIME not null,
        foreign key(trainer_id) references trainers
    );

create table if not exists admins
    (
        admin_id SERIAL,
        email varchar(255),
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
        status varchar(255),
        primary key(room_number)
    );

create table if not exists schedules
    (
        schedule_id SERIAL,
        room_number int not null,
        primary key(schedule_id),
        foreign key(room_number) references rooms
    );

create table if not exists classes 
    (
        class_id SERIAL,
        instructor varchar(255) not null,
        quantity int,
        class_name varchar(255) not null,
        isFull boolean,
        primary key(class_id)
    );

create table if not exists Equipment
    (
        equipment_id SERIAL,
        name varchar(255) not null,
        status varchar(255)
    );