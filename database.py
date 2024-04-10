import hashlib

def create_user_database():
    database_filename = "user_database.txt"

    users = {
        "user1": "password1",
        "user2": "password2",
    }

    try:
        with open(database_filename, "w") as file:
            for username, password in users.items():
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                file.write(f"{username}:{hashed_password}\n")
        
        print(f"User database created successfully: {database_filename}")
    
    except Exception as e:
        print(f"Error creating user database: {e}")

create_user_database()
