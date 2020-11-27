import pyAesCrypt, hashlib
import os
import sys

class Decrypt():

	def __createReqDirs(self):
		try:
			os.mkdir("encryptMe")
		except Exception as e:
			pass

		try:
			os.mkdir(".encrypted")
		except Exception as e:
			pass

	def decrypt(self):

		self.__createReqDirs()

		targetPath = os.path.expanduser('./encryptMe')
		encryptMe = os.path.expandvars(targetPath)

		targetPath = os.path.expanduser('./.encrypted')
		encrypted = os.path.expandvars(targetPath)

		for _, _, files in os.walk(encrypted):
			for file in files:
				try:
					pyAesCrypt.decryptFile(encrypted+"/"+str(file), encryptMe+"/"+str(file)[0:-5], self.__key, 64 * 1024)
					os.remove(encrypted+"/"+str(file))
				except Exception as error:
					continue
					# print(encryptMe+"/"+str(file)[0:-5])
                    # quit()



	def __init__(self, key):
		self.__key = key
        # self.encrypt()




