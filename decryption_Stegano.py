# Decryption Script
import cv2

def decrypt_Image(image_Path, password):
    img = cv2.imread(image_Path)

    if img is None:
        print("Image Not Found!")
        return False

    c = {}

    for i in range(256):
        c[i] = chr(i)

    m, n, z = 0, 0, 0

    length_Str = ""
    for i in range(8):
        length_Str += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3
    
    # print("length_Str -> ", length_Str)

    try:
        message_Length = int(length_Str)
    except ValueError:
        print("Decryption Failed: Invalid Length Header")
        return False

    message = ""
    for i in range(message_Length):
        message += c[img[n, m, z]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    # print("message -> ", message)

    embedded_Password = message[:len(password)]
    # print("embedded_Password -> ", embedded_Password)
    if embedded_Password != password:
        print("Authentication Failed: Incorrect Password.")
        return False

    decrypted_Message = message[len(password):]
    print("Decrypted Message ->", decrypted_Message)


if __name__ == "__main__":
    image_Path = "encrypted_Image.png"
    password = input("Enter the Password -> ")
    decrypt_Image(image_Path, password)