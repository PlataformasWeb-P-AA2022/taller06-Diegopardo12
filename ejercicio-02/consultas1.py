from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 
from genera_base import Pais


from genera_base import engine

Session = sessionmaker(bind=engine)
session = Session()



pais_uno = session.query(Pais).filter(or_((Pais.continente=="NA", Pais.continente=="SA", Pais.continente=="CA"))).all()
print(pais_uno)
