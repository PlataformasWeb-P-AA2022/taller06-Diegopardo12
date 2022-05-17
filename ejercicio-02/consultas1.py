from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_ 
from genera_base import Pais


from configuracion import engine

Session = sessionmaker(bind=engine)
session = Session()

countrycodes = session.query(Docente).all() 

print("Presentación de todos los Docentes")
for s in docentes:
    print("%s" % (s))
    print("---------")