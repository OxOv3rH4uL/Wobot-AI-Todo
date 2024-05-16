import mysql.connector as db 
import os 
from dotenv import load_dotenv
load_dotenv()

def get_connection():
    connection = db.connect(
        host='mysql',
        username='root',
        password='root',
        database='wobotai',
        port=3306
    )
    return connection

def database_setup():
    try:
        connection = db.connect(
        host='mysql',
        username='root',
        password='root',
        port=3306
        )
        cursor = connection.cursor(dictionary=True)
        # cursor.execute("show databases like 'wobotai'")
        # res = cursor.fetchone()
        # if res is None:
        cursor.execute("create database if not exists wobotai")
        cursor.execute("use wobotai")
        cursor.execute("create table if not exists users(id int primary key auto_increment,username varchar(255) not null,password varchar(255) not null)")
        cursor.execute("create table if not exists todos(id int primary key auto_increment,uid int,title varchar(255) not null,description text not null,status varchar(255),foreign key (uid) references users(id) on delete cascade)")
    except db.Error as e:
        print("Error setting up the database : ",e)
