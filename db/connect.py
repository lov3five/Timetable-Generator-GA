import os
import mysql_helper
from mysql_helper import connect_to_mysql
from dotenv import load_dotenv
load_dotenv()

# Info MySQL Server
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Connect to MySQL database
mydb = connect_to_mysql(DB_HOST, DB_NAME, DB_USER, DB_PASSWORD)
if mydb is None:
    print("Connection to MySQL database failed!")
    exit(1)
    
mycursor = mydb.cursor()

# DATABASE OF TIMETABLE GENERATOR GA
# Create table subjects
# TODO: NULL
mycursor.execute("""
CREATE TABLE IF NOT EXISTS subjects (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    number_of_periods VARCHAR(255) NULL
)
""")
# Create table instructors
mycursor.execute("""
CREATE TABLE IF NOT EXISTS instructors (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL, 
    name VARCHAR(60) NOT NULL, 
    sex VARCHAR(10), 
    email VARCHAR(40) NULL, 
    phone_number VARCHAR(15) NULL,
    address VARCHAR(255) NULL
)
""")

# Create table instructors_subjects (Bảng trung gian thể hiện mối quan hệ N-N giữa instrucors và subjects)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS instructors_subjects (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    subject_id INT NOT NULL,
    instructor_id INT NOT NULL,
    FOREIGN KEY (subject_id) REFERENCES subjects(id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(id)
)
""")

# Create table populations
mycursor.execute("""
CREATE TABLE IF NOT EXISTS populations (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    size INT NOT NULL,
    generation INT,
    fitness DECIMAL(10.3)
)   
""")

# TODO: NULL
# Create table schedules
mycursor.execute("""
CREATE TABLE IF NOT EXISTS schedules (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    population_id INT NOT NULL,
    fitness DECIMAL(10.3) NULL
)
""")

# TODO: NULL
# Create table courses
mycursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(255) NOT NULL,
    max_students INT NOT NULL,
    instructor_subject_id INT NOT NULL,
    schedules_id INT ,
    FOREIGN KEY (instructor_subject_id) REFERENCES instructors_subjects(id),
    FOREIGN KEY (schedules_id) REFERENCES schedules(id)
)
""")

# Create table timelessons
mycursor.execute("""
CREATE TABLE IF NOT EXISTS timelessons (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    uuid VARCHAR(6) NOT NULL,
    period VARCHAR(255)
)
""")

# Create table rooms
mycursor.execute("""
CREATE TABLE IF NOT EXISTS rooms (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(15) NOT NULL,
    capacity INT NOT NULL,
    type VARCHAR(15)
)
""")

# Create table rooms_timelessons (Bảng trung gian thể hiện mối quan hệ N-N giữa rooms và timelessons)
mycursor.execute("""
CREATE TABLE IF NOT EXISTS rooms_timelessons (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    room_id INT NOT NULL,
    timelesson_id INT NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms(id),
    FOREIGN KEY (timelesson_id) REFERENCES timelessons(id)
)
""")



        
