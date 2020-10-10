from models import Utilisateur
import sqlalchemy
from sqlalchemy.orm import sessionmaker
import session

engine = sqlalchemy.create_engine("mysql://root:@localhost/evesurvey", echo=False)

Session = sessionmaker(bind=engine)

session = Session()

def save_utilisateur(utilisateur: Utilisateur) -> bool:
    """
    Cette fonction enregistre un utilisateur
    """
    try:
        session.add(utilisateur)
        session.commit()
    except Exception as exception:
        print(exception)
        return False
    else:
        return True
    finally: session.flush()

def update_utilisateur(utilisateur: Utilisateur, id: int) -> bool:
    """
    Cette fonction met à jour l'utilisateur dont l'id est passé en deuxieme 
    parametre par les nouveaux parametres passés en premier parametre
    """
    try:
        x = session.query(Utilisateur).get(id)
        x = utilisateur
        session.commit()
    except Exception as exception:
        print(exception)
        return False
    else:
        return True
    finally: session.flush()

def delete_utilisateur(id: int) -> bool:
    """
    Cette fonction supprime un utilisateur dont l'id est passé en parametre
    """
    try:
        x = session.query(Utilisateur).get(id)
        x.delete()
        session.commit()
    except Exception as exception:
        print(exception)
        return False
    else:
        return True
    finally: session.flush()

def get_all_utilisateurs():
    """
        Cette fonction renvoit tous les utilisateurs
    """
    utilisateurs = []
    try:
        utilisateurs = session.query(Utilisateur).all()
    except Exception as error:
        print(error)
    finally:
        return utilisateurs

def get_user(id: int) -> Utilisateur:
    """
        Cette fonction renvoit un utilisateur précis dont l'id est specifié en paramètre
    """
    utilisateur = None
    try:
        utilisateur = session.query(Utilisateur).get(id)
    except Exception as error:
        print(error)
    finally:
        return utilisateur

def login_user(email: str, password:str) -> list:

    import time

    utilisateur = None
    try:
        utilisateur = session.query(Utilisateur).filter(Utilisateur.email==email, Utilisateur.password == password)
        list_users = list(utilisateur)
        if list_users != []:
            response = session.set_session(list_users[0])
            time.sleep(2.5)
                      
    except Exception as error:
        return False
    finally:
        return list(utilisateur)

if __name__ == "__main__":
    user = Utilisateur(nom_complet = "Kornelius", email="titi@toto.com", password="12345", adresse="ici", type="admin")
    save_utilisateur(user)

