def user_login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "password123":
        print("Login successful!")
        return True
    else:
        print("Invalid credentials!")
        return False
