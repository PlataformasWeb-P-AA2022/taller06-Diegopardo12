
#pais_dos = session.query(Pais).filter(Pais.continente =="AS").order_by(Pais.dial).all()
#print(pais_dos)


from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import and_, or_  
  
from genera_base import engine
from genera_base import Pais
  
  
 Session = sessionmaker(bind=engine) 
 session = Session() 
  
 print("--------------------------------") 
  
 paises = session.query(Pais).filter((Pais.continente=="AS")).order_by(Pais.dial).all() 
 print(paises) 
  
 print("--------------------------------")