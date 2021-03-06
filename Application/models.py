from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

# Creation du model des utilisateurs

Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = "utilisateurs"
    id = Column(Integer, primary_key=True)
    nom_complet = Column(String)
    email = Column(String)
    password = Column(String)
    adresse = Column(Text)
    type = Column(String)

    def __str__(self):
        return f"id: {self.id}, Nom Complet: {self.nom_complet}, Email: {self.email}, adresse: {self.adresse}"

class Camera(Base):
    __tablename__ = "cameras"
    id = Column(Integer, primary_key=True)
    adresse = Column(String)

    def __str__(self):
        return f'Caméra - {self.adresse}'

