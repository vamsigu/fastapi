from fastapi import APIRouter, Depends
from .. import schemas, models, database
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..Oauth2 import get_current_user

router = APIRouter(
    prefix = "/user",
    tags = ["Users"]
)

get_db = database.get_db

@router.post('/', response_model= schemas.ShowUser, status_code=201)
def create_user(user: schemas.User,db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    new_user= models.User(name= user.name, email= user.email, password= Hash.bcrypt(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/{id}', response_model= schemas.ShowUser, status_code=200)
def get_user(id:int, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code= 404, detail=f"user with id {id} not found")
    return user