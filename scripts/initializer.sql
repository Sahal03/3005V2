create table members 
    (
        member_id SERIAL,
        first_name varchar(255) not null,
        last_name varchar(255) not null,
        phone_number varchar(15),
        primary key(member_id)
    );

create table goals
    (
       member_id int, 
       weight FLOAT,
       time DATE,
       streak int ,
       foreign key(member_id) references members
    );

create table trainers
    (
        trainer_id SERIAL,
        first_name varchar(255) not null,
        last_name varchar(255) not null,
        phone_number varchar(15),
        salary FLOAT,
        primary key(trainer_id)
    );

create table availabilities
    (
        trainer_id int,
        day DATE not null,
        start_time TIME not null,
        end_time TIME not null,
        foreign key(trainer_id) references trainers
    );

create table admins
    (
        admin_id SERIAL,
        salary FLOAT,
        position varchar(255),
        last_name varchar(255) not null,
        first_name varchar(255) not null,
        primary key(admin_id)
    );

create table rooms
    (
        room_number int not null unique,
        name varchar(255),
        status varchar(255),
        primary key(room_number)
    );

create table schedules
    (
        schedule_id SERIAL,
        room_number int not null,
        primary key(schedule_id),
        foreign key(room_number) references rooms
    );

create table classes 
    (
        class_id SERIAL,
        instructor varchar(255) not null,
        quantity int,
        class_name varchar(255) not null,
        isFull boolean,
        primary key(class_id)
    );

create table equipments
    (
        equipment_id SERIAL,
        name varchar(255) not null,
        status varchar(255)
    );