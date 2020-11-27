import pyAesCrypt, hashlib
import os
import sys

class Encrypt():
    def __saveKey(self):
        try:
            with open(".key.txt", "w") as file:
                hashedKey = hashlib.sha512(self.__key.encode())
                file.write(hashedKey.hexdigest())
        except Exception as error:
            print(error)
            quit()

    def __createReqDirs(self):
        try:
            os.mkdir("encryptMe")
        except Exception as e:
            pass

        try:
            os.mkdir(".encrypted")
        except Exception as e:
            pass

    def encrypt(self):
        self.__createReqDirs()

        targetPath = os.path.expanduser('./encryptMe')
        encryptMe = os.path.expandvars(targetPath)

        targetPath = os.path.expanduser('./.encrypted')
        encrypted = os.path.expandvars(targetPath)

        for _, _, files in os.walk(encryptMe):
            for file in files:
                try:
                    pyAesCrypt.encryptFile(encryptMe+"/"+str(file), encrypted+"/"+str(file)+".lock", self.__key, 64 * 1024)
                    os.remove(encryptMe+"/"+str(file))
                except Exception as error:
                    print(error)
                    quit()



    def __init__(self, key):
        self.__key = key
        self.__saveKey()
        # self.encrypt()

if __name__ == '__main__':
    enc = Encrypt()
    enc.encrypt()


