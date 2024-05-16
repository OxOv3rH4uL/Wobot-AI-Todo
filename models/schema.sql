create database if not exists wobotai;
use wobotai;
create table if not exists users(
    id int primary key auto_increment,
    email varchar(255) not null,
    password varchar(255) not null
);

create table if not exists todos(
    id int primary key auto_increment,
    uid int,
    title varchar(255) not null,
    description text not null,
    status varchar(255),
    foreign key (uid) references users(id) on delete cascade
);