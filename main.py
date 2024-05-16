from fastapi import Depends, FastAPI , HTTPException,status
import helpers.connector as database
import helpers.hash as hash
from helpers.enum import Status
from models.models import User , Todo , TokenData
import logging
from helpers.authenticator import *
from helpers.tokens import *
from helpers.oauth2 import get_current_user
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from pydantic import ValidationError


logging.getLogger('passlib').setLevel(logging.ERROR)

async def lifespan(app):
    database.database_setup()
    print("Starting")
    yield
    print("Shutting Down")

app = FastAPI(lifespan=lifespan)



@app.get('/')
async def home():
    return {"message":"Welcome to WOBOT AI TODO API. Signup/Login to view your Todos"}

@app.post('/signup')
async def signup(user: User):
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT id FROM users WHERE username = %s', (user.username,))
    found = cursor.fetchone()
    try:
        if found is None:
            hashed_password = hash.hash_password(user.password)
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (user.username, hashed_password))
            conn.commit()  
            return {"message": "Account Created Successfully"}
        else:
            raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail="Username already exists")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,detail="Username already exists")
    
    finally:
        cursor.close()
        conn.close()


@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user["username"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/todos")
async def get_all_todos(current_user: TokenData = Depends(get_current_user)):
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("select id from users where username = %s", (current_user.username,))
        found = cursor.fetchone()
        cursor.execute("select * from todos where uid = %s",(found['id'],))
        todos = cursor.fetchall()
        cursor.close()
        conn.close()
        return todos
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))



@app.get("/todos/{id}")
async def get_a_todo(id:int , current_user:TokenData = Depends(get_current_user)):
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("select id from users where username = %s", (current_user.username,))
        found = cursor.fetchone()
        cursor.execute("select * from todos where id = %s and uid = %s", (id,found['id']))
        todos = cursor.fetchone()
        cursor.close()
        conn.close()
        if(todos is not None):
            return todos
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo Item Not Found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))


@app.post("/todos")
async def create_todo(request:Todo,current_user: TokenData=Depends(get_current_user)):
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        Todo(**request.model_dump())
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Status should be either pending or completed")
    try:
        cursor.execute("select id from users where username = %s", (current_user.username,))
        found = cursor.fetchone()
        cursor.execute("insert into todos(title,description,status,uid) values(%s,%s,%s,%s)",(request.title,request.description,request.status,found['id'],))
        conn.commit()
        cursor.close()
        conn.close()
        return {"message":"Todo Added Successfully!"}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Server Issue")

@app.patch("/todos/{id}")
async def update_todo(id:int,request:Todo,current_user:TokenData=Depends(get_current_user)):
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        Todo(**request.model_dump())
    except ValidationError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Status should be either pending or completed")
    
    try:
        cursor.execute("select id from users where username = %s", (current_user.username,))
        found = cursor.fetchone()
        cursor.execute("select uid from todos where id = %s", (id,))
        idpres = cursor.fetchone()
        if(idpres is not None):
            cursor.execute("update todos set title = %s , description = %s , status = %s where id = %s and uid = %s",(request.title,request.description,request.status,id,found['id']))
            conn.commit()
            cursor.close()
            conn.close()
            return {"message":"Todo Updated Successfully!"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo Item Not Found")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))

@app.delete("/todos/{id}")
async def delete_todo(id:int,current_user:TokenData=Depends(get_current_user)):
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("select id from users where username = %s", (current_user.username,))
        found = cursor.fetchone()
        cursor.execute("select uid from todos where id = %s", (id,))
        idpres = cursor.fetchone()
        if idpres is not None:
            cursor.execute("delete from todos where uid = %s and id = %s", (found['id'],id,))
            conn.commit()
            cursor.close()
            conn.close()
            return {"message":"Todo Deleted Successfully!"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Todo Item Not Found!")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail=str(e))


