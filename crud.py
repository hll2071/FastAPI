from sqlalchemy.orm import Session
from models import Diary

def get_diaries(db: Session):
    return db.query(Diary).all()

def get_diary(db: Session, diary_id: int):
    return db.query(Diary).filter(Diary.id == diary_id).first()

def create_diary(db: Session, title: str, content: str):
    new_diary = Diary(title=title, content=content)
    db.add(new_diary)
    db.commit()
    db.refresh(new_diary)
    return new_diary

def update_diary(db: Session, diary_id: int, title: str, content: str):
    diary = db.query(Diary).filter(Diary.id == diary_id).first()
    if diary:
        diary.title = title
        diary.content = content
        db.commit()
    return diary

def delete_diary(db: Session, diary_id: int):
    diary = db.query(Diary).filter(Diary.id == diary_id).first()
    if diary:
        db.delete(diary)
        db.commit()
