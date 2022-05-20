from sqlalchemy import create_engine

engine = create_engine('sqlite:///basdemo.db')

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Pais(Base):
    __tablename__ = 'countrycodes'
    
    id = Column(Integer, primary_key=True)
    nombre_pais = Column(String(200))
    capital = Column(String(200))
    continente = Column(String(200))
    dial = Column(String(200))
    geoname_ID = Column(String(200))
    itu = Column(String(200))
    lenguajes = Column(String(200))
    idependiente = Column(String(200))

def __repr__(self):
        return "Países:  País=%s Capital=%s Continente:%s DIAL=%s GEONAME_ID:%s ITU=%s Lenguaje:%s Independencia=%s" %(
                          self.nombre_pais,
                          self.capital,
                          self.continente,
                          self.dial,
                          self.geoname_ID,
                          self.itu,
                          self.lenguajes,
                          self.idependiente)


Base.metadata.create_all(engine)