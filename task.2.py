from PIL import Image
import numpy as np
import hashlib

def generate_key(password):
    return int(hashlib.sha256(password.encode()).hexdigest(), 16) % 256

def encrypt_image(image_path, password):
    img = Image.open(image_path)
    arr = np.array(img)

    key = generate_key(password)

    flat = arr.flatten()

    np.random.seed(key)
    indices = np.arange(len(flat))
    np.random.shuffle(indices)

    flat = flat[indices]

    flat = flat ^ key

    encrypted = flat.reshape(arr.shape)

    Image.fromarray(encrypted.astype(np.uint8)).save("encrypted.png")

    np.save("shuffle_key.npy", indices)

    print("Image Encrypted Successfully!")

def decrypt_image(image_path, password):
    img = Image.open(image_path)
    arr = np.array(img)

    key = generate_key(password)

    flat = arr.flatten()

    flat = flat ^ key

    indices = np.load("shuffle_key.npy")

    original = np.zeros_like(flat)
    original[indices] = flat

    decrypted = original.reshape(arr.shape)

    Image.fromarray(decrypted.astype(np.uint8)).save("decrypted.png")

    print("Image Decrypted Successfully!")

while True:
    print("\n===== ADVANCED IMAGE ENCRYPTION =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        path = input("Image Path: ")
        password = input("Password: ")
        encrypt_image(path, password)

    elif choice == "2":
        path = input("Encrypted Image Path: ")
        password = input("Password: ")
        decrypt_image(path, password)

    elif choice == "3":
        break

    else:
        print("Invalid Choice")