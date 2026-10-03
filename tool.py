from cryptography.fernet import Fernet
import os

def generate_key():
    if os.path.exists("secret.key"):
        print("Key already exists. Delete it manually if you really want a new one.")
        return False
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    return True


#generate_key()

def load_key():
    with open("secret.key", "rb") as f:
        return f.read()
def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filename + ".enc","wb") as file:
        file.write(encrypted)

#encrypt_file("note.txt")

def decrypt_file(filename):
    key = load_key()
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    decrypted = f.decrypt(data)
    with open("decrypted_" + filename[:-4], "wb") as file:
        file.write(decrypted)

#decrypt_file("note.txt.enc")

def main():
    print("1) Generate key")
    print("2) Encrypt file")
    print("3) Decrypt file")

    choice = input("Choose: ")

    if choice == "1":
        if generate_key():
         print("Key saved to secret.key")

    elif choice == "2":
        name = input("File name: ")
        encrypt_file(name)
        print("Encrypted: ", name + ".enc")

    elif choice == "3":
        name = input("Encrypted File name: ")
        decrypt_file(name)
        print("Decrypted successfully")

    else:
        print("Invalid option")

main()