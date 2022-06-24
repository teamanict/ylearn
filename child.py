from app import db
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Child(Base):
    __tablename__ = "childs"
    child_id = db.Column(Integer, primary_key=True)
    first_name = db.Column(String)
    last_name = db.Column(String)
   # parent = relationship("Parent", backref=backref("children"))

def createChild(fname, lname):
    c = Child(first_name=fname, last_name=lname)
    db.session.add()
    db.session.commit()
    return c

createChild('ferty', 'joe')  

'''
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, session


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/Student/Desktop/edutech/db.db3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
'''

