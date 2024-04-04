from personnes.personne import Personne, ListePersonne
import database as db


    # La classe ListePersonneDAO remplie les exigeances du premier travail du chapitre 1:
    #       " Gestion d'une liste d'objets "
    #

class ListePersonneDAO:
    # Attributs de la classe #
    connexion = db.connexion()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

        # # # CRUD classmethods # # #

    # CREATE
    @classmethod
    def ajouter_personne(cls, pers:Personne):
        sql = "INSERT into personnes(nom, age) VALUES(%s,%s)"
        parameters = (pers.nom, pers.age)

        try:
            ListePersonneDAO.cursor.execute(sql, parameters)
            ListePersonneDAO.connexion.commit()
            ListePersonneDAO.cursor.close()
            message = f"La personne nommée '{pers.nom}' a bien été ajoutée."
        except Exception as error:
            message = f"Une erreur est survenue lors de l'ajout de la personne '{pers.nom}'. "

        return message
    
    # READ
    @classmethod
    def afficher_personnes(cls):
        sql = "SELECT * FROM personnes"
        try:
            ListePersonneDAO.cursor.execute(sql)
            personnes = ListePersonneDAO.cursor.fetchall()
            message = "sucess"
        except Exception as error:
            message = "Une erreur est survenue lors de la récuperation des données."
            personnes = []
        return(personnes, message)
    
    @classmethod
    def rechercher_personne(cls, value):
        sql = "SELECT * FROM personnes where nom=%s"
        ListePersonneDAO.cursor.execute(sql, (value,))
        personne = ListePersonneDAO.cursor.fetchone()
        ListePersonneDAO.cursor.close()
        return personne

    # UPDATE
    @classmethod
    def update(cls, nom, age):
        sql = "UPDATE FROM personnes SET age=%s WHERE nom=%s"
        ListePersonneDAO.cursor.execute(sql, (age, nom))
        ListePersonneDAO.connexion.commit()
        ListePersonneDAO.cursor.close()

        return f"L'age de la personne nommée {nom} a bien été changé par {age}!"
    # DELETE
    @classmethod
    def delete(cls, value):
        sql = "DELETE FROM personnes WHERE nom=%s"
        ListePersonneDAO.cursor.execute(sql, (value))
        ListePersonneDAO.connexion.commit()
        ListePersonneDAO.cursor.close()

        return f"La personne au nom de {value} a bien été supprimée."
    
    @classmethod
    def filtrer_personne_par_age(cls, min_age, max_age):
        sql = "SELECT * FROM Personnes WHERE age BETWEEN %s and %s"
        ListePersonneDAO.cursor.execute(sql, (min_age, max_age))
        superliste = ListePersonneDAO.cursor.fetchall()
        
        if superliste:
            print(f"Liste des personnes dont l'age est compris entre {min_age} et {max_age}")
            print("=-=  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  -  =-=")
            for personne in superliste:
                print(f"Nom : {personne[0]} |  Age : {personne[1]}")
                print("-------------------------------------------\n")
        else:
            print(" AUCUN RÉSULTAT TROUVÉ !")

        ListePersonneDAO.cursor.close() ; 
        ListePersonneDAO.connexion.close()
    





    