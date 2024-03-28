import mysql.connector as maitreyoda

def connexion():
    db_con = maitreyoda.connect(
        user="root",
        password="",
        host="localhost",
        database="cinema"
    )
    return db_con