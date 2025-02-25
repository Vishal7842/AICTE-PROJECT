import cv2
import os
def decrypt_message(image_path):
    # Load the encrypted image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found or unable to load.")
        return
    # Read the password from the file
    with open("password.txt", "r") as f:
        stored_password = f.read().strip()
    # Input passcode for decryption
    pas = input("Enter passcode for Decryption: ")
    if stored_password == pas:
        message = ""
        n, m, z = 0, 0, 0
        # Read the message length from the file
        with open("message_length.txt", "r") as f:
            message_length = int(f.read().strip())
        print("Message Length:", message_length)
        # Create a dictionary for character decoding
        c = {i: chr(i) for i in range(255)}
        # Decrypt the message from the image
        for i in range(message_length):
            pixel_value = img[n, m, z]
            print(f"Pixel Value at ({n}, {m}, {z}):", pixel_value)  # Debugging pixel value
            message += c[pixel_value]
            n += 1
            m += 1
            z = (z + 1) % 3
        print("Decryption message:", message)
        # Optionally, read the secret message from the text file
        with open("secret_message.txt", "r") as f:
            original_message = f.read().strip()
        print("Original Secret Message from file:", original_message)
    else:
        print("YOU ARE NOT auth")
# Example usage of the decryption function
if __name__ == "__main__":
    decrypt_message("encryptedImage.jpg")  # Replace with your encrypted image path