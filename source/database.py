from sqlalchemy import create_engine,Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# CONSTANTS
#*****************************************************
SERVER= "postgres_server"
PORT=   "5432"
USER =  "postgres"
PWD =   "postgres"
DATABASE="postgres"
#*****************************************************


# Method:       add()
# Descripcion:  Método que permite agregar registros a la tabla Result
# Params:       xUuid= Identificador unico del proceso, xorder= orden de los registros, xvalue= valor
# Return:       
def add(xUuid, xorder,xvalue, xPos_x, xPos_y):
  new_result = Result(uuid=xUuid, order=xorder, value=xvalue, pos_x=xPos_x, pos_y=xPos_y)
  session.add(new_result)
  session.commit()


# Class:        Result()
# Descripcion:  Clase qeu define la estructura de la tabla Result para el ORM
class Result(Base):
    __tablename__ = 'result'
    uuid=Column('uuid', String(36),primary_key=True)
    order=Column('order', Integer,primary_key=True)
    value=Column('value', Integer)
    pos_x=Column('pos_x', Integer)
    pos_y=Column('pos_y', Integer)
   

# PROCESS INIT
 
engine = create_engine('postgresql://' + USER +':' + PWD + '@' + SERVER + ':' + PORT + '/' + DATABASE)
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()




