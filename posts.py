
from unittest import skipUnless
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
import schemas, database, models
from sqlalchemy.orm import Session
from database import get_db
from typing import List, Optional
import oauth2
from sqlalchemy import func



router = APIRouter( 
    prefix ='/posts',
    tags = ['Posts']
)

@router.delete('/{id}', response_model=List[schemas.Post])
def delete_post(id: int, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    #index = find_index_post(id)
    #my_posts.pop(index)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"There is no post with id: {id}")
    
    if post.owner_id != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized for requested action")

    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    #cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s,%s,%s) RETURNING * """, (post.title, post.content, post.published))
    #new_post = cursor.fetchone()
    #conn.commit()
    #post_dict = post.dict()
    #post_dict['id'] = randrange (0, 1000000)
    #my_posts.append(post.dict())
    print(get_current_user.email)
    new_post = models.Post(owner_id=get_current_user.id, **post.dict())
    if new_post.owner_id != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized for requested action")

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post
    #return new_post

@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ''):
    
    #posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    results =  db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()

    print (results)
    return results

#@app.get('/posts')
#def get_posts():
#    cursor.execute("""SELECT * FROM posts""")
#    posts = cursor.fetchall()
#    print(posts)
#    return{"data": posts}

@router.get("/{id}")
def get_post(id: str, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):

    #post = db.query(models.Post).filter(models.Post.owner_id == id).all
    
    post =  db.query(models.Post, func.count(models.Vote.post_id).label('votes')).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    print(post) 
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found ")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'message': f"post with id: {id} was not found "}
    return post

@router.put("/{id}")
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), get_current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    #db.add(new_post)
    #db.commit()
    #db.refresh(new_post)
    #index = find_index_post(id)
    #cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
    #conn.commit()
    #updated_post = cursor.fetchone()
    if post == None:
    #if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"There is no post with id: {id}")
    if post.owner_id != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized for requested action")
    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    #post_dict = post.dict()
    #post_dict['id'] = id
    #my_posts[index] = post_dict
    return post_query.first()
    #return Response(status_code=status.HTTP_204_NO_CONTENT)
    #print(post)
    #return {"message": "updated post"}