import pickle
import sys, os

_path_session = os.path.join("config", "session.dat") # The session file's path

def get_session():
    # Load the session's user object
    utilisateur = None

    global _path_session

    try:
        with open(_path_session, "rb") as fichier:
            unpickler = pickle.Unpickler(fichier)
            utilisateur = unpickler.load()
    except IOError as error:
        pass
    
    return utilisateur

def set_session(utilisateur):
    # Dump ths user in session

    global _path_session

    try:
        with open(_path_session, "wb") as fichier:
            pickler = pickle.Pickler(fichier)
            pickler.dump(utilisateur)
    except IOError as error:
        sys.stderr.write("Erreur d'entree-sortie")
        return False
    else:
        return True

def _get_session_path() -> str:
    # The path of the session_file
    return _path_session