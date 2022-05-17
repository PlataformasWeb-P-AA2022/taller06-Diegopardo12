from sqlalchemy import create_engine

engine = create_engine('sqlite:///basdemo.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'countrycodes'
    
    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String)
    capital = Column(String)
    continente = Column(String)
    dial = Column(String)
    geoname_ID = Column(String)
    itu = Column(String)
    lenguajes = Column(String)
    idependiente = Column(String)


Base.metadata.create_all(engine)