import cv2
import os
def encrypt_message(image_path, secret_message, password):
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found or unable to load.")
        return
    # Create character mapping
    d = {chr(i): i for i in range(255)}
    # Encrypt the message into the image
    m, n, z = 0, 0, 0
    for char in secret_message:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3
    # Save the encrypted image
    cv2.imwrite("encryptedImage.jpg", img)
    # Save the secret message to a text file
    with open("secret_message.txt", "w") as f:
        f.write(secret_message)
    # Save the password to a file
    with open("password.txt", "w") as f:
        f.write(password)
    # Save the message length to a file
    with open("message_length.txt", "w") as f:
        f.write(str(len(secret_message)))
    print("Message encrypted and saved as 'encryptedImage.jpg'.")
# Example usage of the encryption function
if __name__ == "__main__":
    secret_message = input("Enter secret message to encrypt: ")
    password = input("Enter a passcode for encryption: ")
    encrypt_message(r"7056362.png", secret_message, password)  # Replace with your image path