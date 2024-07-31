from fastapi import FastAPI, status, Body, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory = "templates")
users = []

class User(BaseModel):
    text: str
    id: int = None



@app.get('/')
def get_all_messages(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "text": users})

@app.get("/users/{user_id}")
def get_message(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "text": users[user_id]})
    except IndexError:
        raise HTTPException(status_code=404, detail='Message not found')

@app.post('/')
def create_user(username:str, age:int):
    username = username
    age = age
def create_message(request: Request, text: str = Form()) -> HTMLResponse:
    if users:
        user_id = max(users, key = lambda u: u.id).id + 1
    else:
        user_id = 0
    users.append(User(id = user_id, text = text))
    return templates.TemplateResponse("users.html", {"request": request, "text": users})
