from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, database, token
from ..hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login')
def login(login: OAuth2PasswordRequestForm = Depends(), db: Session= Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == login.username).first()
    if not user:
        raise HTTPException(status_code= 404, detail="invalid credentials")
    if not Hash.verify(login.password, user.password):
        raise HTTPException(status_code=404, detail='incorrect password')
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}