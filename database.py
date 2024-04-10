import hashlib

def create_user_database():
    database_filename = "user_database.txt"

    users = {
        "user1": ("password1", "user1@example.com"),
        "user2": ("password2", "user2@example.com"),
    }

    try:
        with open(database_filename, "w") as file:
            for username, data in users.items():
                password, email = data
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
                file.write(f"{username}:{hashed_password}:{email}\n")
        
        print(f"User database created successfully: {database_filename}")
    
    except Exception as e:
        print(f"Error creating user database: {e}")

create_user_database()
