from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 
from genera_base import Pais


from genera_base import engine

Session = sessionmaker(bind=engine)
session = Session()

pais_cinco = session.query(Pais).filter(and_(Pais.nombre_pais.like("%uador%"), Docente.capital.like("%ito%"))).all()
print(pais_cinco)