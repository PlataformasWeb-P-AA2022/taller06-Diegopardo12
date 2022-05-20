from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 
from genera_base import Pais


from genera_base import engine

Session = sessionmaker(bind=engine)
session = Session()



pais_tres = session.query(Pais).filter(Pais.lenguajes).all()
print(pais_tres)


