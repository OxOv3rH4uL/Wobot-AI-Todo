import mysql.connector as db 
import os 
from dotenv import load_dotenv
load_dotenv()

def get_connection():
    """
    To get connection to MYSQL
    """
    connection = db.connect(
        host=os.getenv("DB_HOST"),
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        database='wobotai',
        port=3306
    )
    return connection

def database_setup():
    """
    Initial setup of Database
    """
    try:
        connection = db.connect(
        host=os.getenv("DB_HOST"),
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        port=3306
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("create database if not exists wobotai")
        cursor.execute("use wobotai")
        cursor.execute("create table if not exists users(id int primary key auto_increment,username varchar(255) not null,password varchar(255) not null)")
        cursor.execute("create table if not exists todos(id int primary key auto_increment,uid int,title varchar(255) not null,description text not null,status varchar(255),foreign key (uid) references users(id) on delete cascade)")
    except db.Error as e:
        print("Error setting up the database : ",e)
