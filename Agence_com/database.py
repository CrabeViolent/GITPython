import mysql.connector as maitreyoda

def connect_db():
    connexion = maitreyoda.connect(
        user = "root",
        password = "",
        database = "agence",
        host = "localhost"
        )
    return connexion