from dbConnection import db, mycursor

def create_database():
    mycursor.execute("CREATE DATABASE IF NOT EXISTS instagram")
    print("Database created successfully")

# create_database()