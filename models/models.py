# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Admin(Base):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True)
    uname = Column(String(20))
    code = Column(String(20))
    password = Column(String(20))


class Sort(Base):
    __tablename__ = 'sorts'

    id = Column(Integer, primary_key=True)
    sname = Column(String(20))


class Sysadmin(Base):
    __tablename__ = 'sysadmin'

    id = Column(Integer, primary_key=True)
    uname = Column(String(20))
    code = Column(String(20))
    password = Column(String(20))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    uname = Column(String(20))
    code = Column(String(20))
    password = Column(String(20))


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    bname = Column(String(20))
    sid = Column(ForeignKey('sorts.id'), index=True)
    number = Column(Integer)
    author = Column(String(20))
    birth = Column(String(20))
    edition = Column(String(20))

    sort = relationship('Sort')


class Borrow(Base):
    __tablename__ = 'borrows'

    id = Column(Integer, primary_key=True)
    uid = Column(ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    bid = Column(ForeignKey('books.id', ondelete='CASCADE', onupdate='CASCADE'), index=True)
    startTime = Column(DateTime)
    endTime = Column(DateTime)
    status = Column(Integer)

    book = relationship('Book')
    user = relationship('User')


class Reserve(Base):
    __tablename__ = 'reserves'

    id = Column(Integer, primary_key=True)
    uid = Column(ForeignKey('users.id'), index=True)
    bkid = Column(ForeignKey('books.id'), index=True)
    startTime = Column(DateTime)
    endTime = Column(DateTime)
    status = Column(Integer)

    book = relationship('Book')
    user = relationship('User')


class Back(Base):
    __tablename__ = 'backs'

    id = Column(Integer, primary_key=True)
    brid = Column(ForeignKey('borrows.id'), index=True)
    status = Column(Integer)

    borrow = relationship('Borrow')
