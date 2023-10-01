import os
import random
import platform
from cryptography.fernet import Fernet

device = platform.system()
def encrrypt():
    loc = input("Enter file path: ")
    key = Fernet.generate_key()
    with open(loc, "rb") as f:
        data = f.read()
    data = Fernet(key).encrypt(data)
    with open(loc, "wb") as f:
        encrypt = f.write(data)
        print("Done encrypting you can unlock using given key.")
        print(key)
    
def main():
    while True:
        os.system('cls')
        print(""" Hello guys I am here to remind you that some precautions should be taken before using it. It is an open-source code \n so if
        someone is catched selling it then I'll stop updating it.""")
        print("This is to help you encode your code in different ways lets move it on \n Point to be noted we dont make it paid we just make it \n ecrypt so no onw will be able to access your code")
        print(" System =", device)
        encrrypt()
main()
