from fileAttentes.fileAttente import FileAttente
from personnes.personne import Personne
import database as db


class fileAttenteDAO:
    # Attributs de la classe #
    connexion = db.connexion()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

    # # # CRUD classmethods # # #

    # CREATE NON-PRIORITAIRE # 
    @classmethod
    def ajouter_personne_en_attente(cls, pers:Personne):

        FileAttente.file_attente.append(pers.nom)
        sql = "INSERT INTO fileattente (nom, grade) VALUES(%s, %s)"
        fileAttenteDAO.cursor.execute(sql, (pers.nom, "non-prioritaire"))

        fileAttenteDAO.connexion.commit()
        fileAttenteDAO.cursor.close()
        fileAttenteDAO.connexion.close()
    # CREATE PRIORITAIRE # 
    @classmethod
    def ajouter_personne_en_attente_prioritaire(cls, pers:Personne):

        FileAttente.file_attente_prioritaire.append(pers.nom)
        sql = "INSERT INTO fileattente (nom, grade) VALUES(%s, %s)"
        fileAttenteDAO.cursor.execute(sql, (pers.nom, "prioritaire"))

        fileAttenteDAO.connexion.commit()
        fileAttenteDAO.cursor.close()
        fileAttenteDAO.connexion.close()

    # SUPPRIMER DE FILE ATTENTE # 
    @classmethod
    def supprimer_personne_de_attente(cls):
        
        sql = "SELECT * FROM FileAttente WHERE grade='non-prioritaire'"
        fileAttenteDAO.cursor.execute(sql)
        file_attente = fileAttenteDAO.cursor.fetchall()

        sql = "SELECT * FROM FileAttente WHERE grade='prioritaire'"
        fileAttenteDAO.cursor.execute(sql)
        file_attente_prioritaire = fileAttenteDAO.cursor.fetchall()

        if file_attente_prioritaire:
            try:
                personne_supprime = file_attente_prioritaire.pop(0)
                message = f"La personne {personne_supprime} a bien été supprimée de la file d'attente PRIORITAIRE."
                sql = "DELETE FROM FileAttente WHERE nom=%s"
                fileAttenteDAO.cursor.execute(sql, (personne_supprime,))
                fileAttenteDAO.connexion.commit()
                fileAttenteDAO.cursor.close()
                fileAttenteDAO.connexion.close()
            except Exception as error:
                message = f" Une erreur est survenue lors de l'opération."
            return message
        
        elif file_attente:
            try:
                personne_supprime = file_attente.pop(0)
                message = f"La personne {personne_supprime} a bien été supprimée de la file d'attente."
                sql = "DELETE FROM FileAttente WHERE nom=%s"
                fileAttenteDAO.cursor.execute(sql, (personne_supprime,))
                fileAttenteDAO.connexion.commit()
                fileAttenteDAO.cursor.close()
                fileAttenteDAO.connexion.close()
            except Exception as error:
                message = f" Une erreur est survenue lors de l'opération."
            return message
        
        else:
            message = "La file d'attente est VIDE."
            return message
        


    
