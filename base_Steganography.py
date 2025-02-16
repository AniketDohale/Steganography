# import os
import cv2

img = cv2.imread("nature.jpg")

encryption_Message = input("Enter Secret Message -> ")
password = input("Enter a Password -> ")

d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

for i in range(len(encryption_Message)):
    img[n, m, z] = d[encryption_Message[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("encrypted_Image.jpg", img)
# os.system("Start encryption_Image.jpg")

message = ""

m = 0
n = 0
z = 0

passwd = input("Enter a Password -> ")

if password == passwd:
    for i in range(len(encryption_Message)):
        message = message + c[img[m, n, z]]
        m = m + 1
        n = n + 1
        z = (z + 1) % 3
    print("Decrypted Message -> ", message)

else:
    print("Authentication Failed..")