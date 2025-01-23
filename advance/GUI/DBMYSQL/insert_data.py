from .dbConnection import db, mycursor

def insert_user_data(email, password):
    query = "INSERT INTO users (email, password) VALUES (%s, %s)"
    values = (email, password)
    mycursor.execute(query, values)
    db.commit()

def check_user_exists(email, password):
    query = "SELECT * FROM users WHERE email = %s AND password = %s"
    values = (email, password)
    mycursor.execute(query, values)
    result = mycursor.fetchone()
    return result is not None