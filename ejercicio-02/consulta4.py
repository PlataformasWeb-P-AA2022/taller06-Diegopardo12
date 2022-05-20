from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 
from genera_base import Pais


from genera_base import engine

Session = sessionmaker(bind=engine)
session = Session()



pais_cuatro = session.query(Pais).filter(Pais.continente=="EU").order_by(Pais.capital).all()
print(pais_cuatro)


