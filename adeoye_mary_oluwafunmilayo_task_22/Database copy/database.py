from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
# from pymysql.constants import CLIENT
from dotenv import load_dotenv
import os 

load_dotenv()

# create a connection database (the dialect is mysql, the driver is pymysql)
# db_url = dialect+driver ://dbuser;dbpassword;dbhost;dbname . This is the format of creating a url


db_url = f"mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}"

engine = create_engine(db_url)

session = sessionmaker(bind=engine)

db = session()

#query = text("select * from user")
#user = db.execute(query).fetchall()

#print(user)

create_users = text("""

CREATE TABLE  IF NOT EXISTS users (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
email VARCHAR(100) NOT NULL,
password VARCHAR(25) NOT NULL

);
                    
""")



create_courses = text("""
                      
CREATE TABLE IF NOT EXISTS courses(
id INT AUTO_INCEREMENT PRIMARY KEY,
title VARCHAR(100) NOT NULL,
level VARCHAR(100) NOT NULL
);
""")

db.execute(create_users)