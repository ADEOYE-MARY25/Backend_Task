from database import db
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
import bcrypt
from dotenv import load_dotenv
import uvicorn
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from pymysql.constants import CLIENT
from dotenv import load_dotenv
import os

load_dotenv()

token_time = os.getenv("token_time")

app = FastAPI(title= "Simple App", version = "1.0.0")


class Simple(BaseModel):
    Name: str = Field(..., examples= "Adeoye Mary")
    email: str = Field(..., examples= "maryadeoye@gmail.com")
    password: str = Field(..., examples= "peace123")
    usertype: str = Field(..., examples=["student"])


class Login(BaseModel):
    email: str = Field(...,  examples=["samadeoye@gmail.com"])   
    password: str = Field(..., example=["1234a"])


class courseRequest(BaseModel):
    title: str = Field(...,  examples=["Algorithms"])
    level: str = Field(..., examples=["400lv"])


class enrollnmentRequest(BaseModel):
    course_id: str = Field(..., examples=["202"])

# Class courseID()    



@app.post("/signup")
def signup(input:Simple):
    try:

        duplicate_query = text("""
            SELECT * FROM users WHERE email = :email
        """)
        
        existing = db.execute(duplicate_query, {"email": input.email}.fetchone()
        if existing:
            return("Email alreadly exists!"))
        
        query=text("""
            INSERT INTO users(name, email, password)
            VALUES(:name, :email, :password)       )
                            """) 
        
        salt=bcrypt.gen_salt()
        hashedpassword = bcrypt.hashpw(input.password.encode('utf-8'), salt)


        db.execute(query, {"name": input.name, "email":input.email, "password":hashedpassword})

    except Exception as e:
        raise HTTPException(status=500, details= str(e))
    
    if__name__= " __main__":
        uvicorn.run(app, host=os.getenv("host"), port= int(os.getenv("port")))

