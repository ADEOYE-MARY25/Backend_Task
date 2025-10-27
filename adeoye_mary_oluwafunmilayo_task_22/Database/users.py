from database import db

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import text
import os
from dotenv import load_dotevn
import uvicorn

import bcrypt


load_dotevn()
app = FastAPI(title="Simple App", version="1.0.0")

class Simple(BaseModel):
    name: str = Field(..., examples=["Sam Larry"])
    email: str = Field(..., examples=["sam@gmail.com"])
    password: str = Field(..., examples=["sam123"])



@app.post("/signup")
def signup(input: Simple):
    try:

        duplicate_query = text("""
                               INSERT INTO users (name, email, password)
                               VALUES (:name, :email, :password)
                               """)


        existing = db.execute(duplicate_query, {"email": input.email})
        if existing:
             print("Email already exists")                               


        query = text("""
                 INSERT INTO users(name, email, password)
                 VALUES (:name, :email, :password)
                 """)
    
        salt = bcrypt.gensalt()
        hashedPassword = bcrypt.hashpw(input.password.encode('utf-8'), salt)


        db.excecute(query, {"name": input.name, "email": input.email, "password":hashedPassword, "usertype": input.user})

    except Exception as e:
        raise HTTPException(status_code=500, detail= str(e))


if __name__ ==" __main__":
    uvicorn.run(app, host=os.getenv("host"), port=int(os.getenv("port")))

