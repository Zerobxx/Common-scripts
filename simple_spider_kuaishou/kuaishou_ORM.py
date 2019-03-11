# coding: utf-8

# 导入:
from sqlalchemy import Column, String, Integer, Boolean, Text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib import parse

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Kuaishou(Base):
    # 表的名字:
    __tablename__ = 'kuaishou_hot'

    # 表的结构:
    id = Column(Integer, primary_key=True)
    kuaishou_id = Column(String(50))
    view = Column(Integer)
    like = Column(Integer)
    comment = Column(Integer)
    user_id = Column(String(50))
    user_name = Column(String(50))
    caption = Column(Text)
    mv_url = Column(Text)
    if_mv = Boolean

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://root:Youfang2019@localhost:3306/kuaishou')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)