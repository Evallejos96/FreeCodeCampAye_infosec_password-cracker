import hashlib

def crack_sha1_hash(hash_to_crack, use_salts=False):
    # Cargar lista de contraseñas
    with open("top-10000-passwords.txt", "r") as file:
        passwords = [p.strip() for p in file.readlines()]

    # Si NO se usan salts
    if not use_salts:
        for password in passwords:
            hashed = hashlib.sha1(password.encode()).hexdigest()
            if hashed == hash_to_crack:
                return password

        return "PASSWORD NOT IN DATABASE"

    # Si se usan salts
    with open("known-salts.txt", "r") as file:
        salts = [s.strip() for s in file.readlines()]

    # Probar combinaciones salt + password y password + salt
    for password in passwords:
        for salt in salts:
            # salt + password
            hashed1 = hashlib.sha1((salt + password).encode()).hexdigest()
            if hashed1 == hash_to_crack:
                return password

            # password + salt
            hashed2 = hashlib.sha1((password + salt).encode()).hexdigest()
            if hashed2 == hash_to_crack:
                return password

    return "PASSWORD NOT IN DATABASE"
