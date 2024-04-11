import database as db
from employes.employe import Employe

class EmployeDao:

    connexion = db.connect_db()
    cursor = connexion.cursor()
    
    def __init__(self) -> None:
        pass


    @classmethod
    def read_one(cls, matricule):
        sql = "SELECT * FROM employe WHERE matricule=%s"
        try:
            cls.cursor.execute(sql, (matricule,))
            employe = cls.cursor.fetchone()
            message = "success"
            return (message, employe)
        except Exception as error:
            message = "error"
            return (message, matricule)
    
    @classmethod
    def update(cls, matricule, nouveau_nom, nouveau_prenom, nouveau_fonction, nouveau_departement):
        sql = "UPDATE employe SET nom=%s, prenom=%s, fonction=%s, departement=%s WHERE matricule = %s"
        try:
            cls.cursor.execute(sql, (nouveau_nom, nouveau_prenom, nouveau_fonction, nouveau_departement, matricule))
            cls.connexion.commit()
            message = "success"
        except Exception as error:
            message = "error"
        return (message, matricule)


    @classmethod
    def delete(cls, matricule):
        sql = "DELETE FROM employe WHERE matricule=%s"
        try:
            cls.cursor.execute(sql, (matricule,))
            cls.connexion.commit()
            message = "success"
        except Exception as error:
            message = "error"
        return (message, matricule)
            

    @classmethod  
    def get_all(cls):
        sql = "SELECT * FROM employe"
        try:
            cls.cursor.execute(sql)
            employes = cls.cursor.fetchall()
            message = "success"
        except Exception as error:
            employes = []
            message = "error"
        return (message, employes)
    
    @classmethod  
    def get_all_matricule(cls):
        sql = "SELECT matricule FROM employe"
        try:
            cls.cursor.execute(sql)
            matricules = cls.cursor.fetchall()
        except Exception as error:
            matricules = []
        return matricules
    
    @classmethod
    def add(cls, employe: Employe):
        sql = "INSERT INTO employe(nom,prenom,matricule,fonction,departement) VALUES(%s,%s,%s,%s,%s)"
        params = (employe.nom, employe.prenom, employe.matricule, employe.fonction, employe.departement)
        try:
            cls.cursor.execute(sql, params)
            cls.connexion.commit()
            message = "success"
        except Exception as error:
            message = "error"
            print(error)
        return (message)
    

