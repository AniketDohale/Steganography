# Encryption Script
import cv2

def encrypt_Image(image_Path, secret_Message, password, output_Path):
    img = cv2.imread(image_Path)

    if img is None:
        print("Image Not Found!")
        return False

    d = {}

    for i in range(256):
        d[chr(i)] = i

    m, n, z = 0, 0, 0

    message = password + secret_Message
    # print("Message -> ", message)
    message_Length = f"{len(message):08d}"
    # print("message_length -> ", message_length)
    full_Message = message_Length + message
    # print("Full Message -> ", full_message)

    for i in range(len(full_Message)):
        img[n, m, z] = d[full_Message[i]]
        n = (n + 1) % img.shape[0]
        m = (m + 1) % img.shape[1]
        z = (z + 1) % 3

    cv2.imwrite(output_Path, img)
    print(f"Message Encrypted and Saved as {output_Path}")


if __name__ == "__main__":
    image_Path = r"img\nature.jpg"
    secret_Message = input("Enter the Message -> ")
    password = input("Enter a Password -> ")
    output_Path = "encrypted_Image.png"

    encrypt_Image(image_Path, secret_Message, password, output_Path)