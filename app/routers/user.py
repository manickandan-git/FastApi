
from .. import models, schemas, utils
from fastapi import Depends, Response,status, HTTPException,APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user.password = utils.hash(user.password)
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[schemas.UserOut])
def get_uers(db: Session = Depends(get_db), response: Response = None):
    users = db.query(models.User).all()
    return users

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db), response: Response = None):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} was not found")  
    return user;    

@router.delete("/{id}",  status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def delete_user(id: int, db: Session = Depends(get_db), response: Response = None):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} was not found")
    user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT) 

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.UserOut)
def update_user(id: int, updated_user: schemas.UserUpdate, db: Session = Depends(get_db), response: Response = None):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} was not found")
    updated_user.password = utils.hash(updated_user.password)
    user.update(updated_user.model_dump(), synchronize_session=False)
    db.commit()
    updated_user_db = db.query(models.User).filter(models.User.id == id).first()
    if not updated_user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id: {id} was not found")
    return updated_user_db
