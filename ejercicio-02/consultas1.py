from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 
from genera_base import Pais


from genera_base import engine

Session = sessionmaker(bind=engine)
session = Session()



pais_uno = session.query(Pais).order_by(Pais.continente=="NA").all()
print(pais_uno)
