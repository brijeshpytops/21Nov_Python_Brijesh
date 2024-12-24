def user_register():
    username = input("Enter username: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    confirm_password = input("Confirm Password: ")

    if password == confirm_password:
        print("Registration Successful!")
    else:
        print("Passwords do not match!")

def otp():
    import random
    otp_code = random.randint(1000, 9999)
    print("One Time Password (OTP):", otp_code)