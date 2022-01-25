#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : domain.py
# @Description:
# @Time       : 2022-1-25 上午 11:18
# @Author     : Hou

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Poems(Base):
    __tablename__ = 'poems'

    id = Column(Integer, primary_key=True)
    poem_verse = Column(String)
    poem_name = Column(String)
    create_time = Column(String)

