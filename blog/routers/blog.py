from fastapi import APIRouter, Depends, HTTPException
from typing import List
from .. import schemas, models, database
from sqlalchemy.orm import Session
from ..Oauth2 import get_current_user



router = APIRouter(
    prefix= "/blog",
    tags= ["Blogs"]
)

get_db = database.get_db

@router.get('/', response_model=List[schemas.showblog], status_code=200)
def all(db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/', status_code = 201)
def create(blog : schemas.Blog, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    new_blog = models.Blog(title = blog.title, description = blog.description)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get('/{id}', response_model=schemas.showblog, status_code=200)
def show(id, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code= 404, detail=f"blog with id {id} not found")
    return blog

@router.delete('/{id}')
def delete(id, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code= 404, detail=f"blog with id {id} not found")
    blog.delete(synchronize_session = False)
    db.commit()
    return 'deleted'

@router.put('/{id}')
def update(id, blog : schemas.Blog,db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code= 404, detail=f"blog with id {id} not found")
    blog.update(blog.dict())
    db.commit()
    return 'updated'