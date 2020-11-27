import sys, os
from conf import *

sys.path.insert(1, os.path.join(ROOT_DIR, "GUI/"))
sys.path.insert(1, os.path.join(ROOT_DIR, "Encryptor/"))

from encrypt import Encrypt
from encrypt_gui import GUI

if __name__ == '__main__':
    proc = Encrypt(sys.argv[1])
    proc.encrypt()

    showProcGUI = GUI()
    showProcGUI.createWindow()


