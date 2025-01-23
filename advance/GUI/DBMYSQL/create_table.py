from dbConnection import db, mycursor

def create_table():
    sql = """CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        );"""
    mycursor.execute(sql)
    

create_table()