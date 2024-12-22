from fastapi import FastAPI, Form, Request, Depends, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from models import Base, get_db, engine
from crud import create_diary, get_diaries, get_diary, update_diary, delete_diary

app = FastAPI()

# DB 초기화
Base.metadata.create_all(bind=engine)

# Jinja2 템플릿 설정
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_diaries(request: Request, db: Session = Depends(get_db)):
    diaries = get_diaries(db)
    return templates.TemplateResponse("index.html", {"request": request, "diaries": diaries})

@app.get("/diary/create")
def create_diary_form(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.post("/diary/create")
def create_diary_post(title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    create_diary(db, title=title, content=content)
    return RedirectResponse("/", status_code=303)

@app.get("/diary/{diary_id}")
def read_diary(diary_id: int, request: Request, db: Session = Depends(get_db)):
    diary = get_diary(db, diary_id=diary_id)
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")
    return templates.TemplateResponse("detail.html", {"request": request, "diary": diary})

@app.get("/diary/{diary_id}/edit")
def edit_diary_form(diary_id: int, request: Request, db: Session = Depends(get_db)):
    diary = get_diary(db, diary_id=diary_id)
    if not diary:
        raise HTTPException(status_code=404, detail="Diary not found")
    return templates.TemplateResponse("update.html", {"request": request, "diary": diary})

@app.post("/diary/{diary_id}/edit")
def edit_diary_post(diary_id: int, title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    update_diary(db, diary_id=diary_id, title=title, content=content)
    return RedirectResponse("/", status_code=303)

@app.post("/diary/{diary_id}/delete")
def delete_diary_post(diary_id: int, db: Session = Depends(get_db)):
    delete_diary(db, diary_id=diary_id)
    return RedirectResponse("/", status_code=303)
