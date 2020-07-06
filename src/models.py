import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=True)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    firstname = Column(String(60), nullable=False)
    lastname = Column(String(60), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    posts = relationship('Post', backref='author', lazy=True)
    followers = relationship('Follower', backref='followers', lazy=True)
    following = relationship('Follower', backref='following', lazy=True)


    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.emal
        }

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    comments = relationship('Comment', backref='post', lazy=True)
    medias = relationship('Media', backref='post', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id
        }

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(255), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id
        }

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    kind = Column(String, nullable=False)
    url = Column(String, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "kind": self.kind,
            "url": self.url,
            "post_id": self.post_id
        }


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')