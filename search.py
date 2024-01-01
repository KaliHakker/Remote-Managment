import os
import sys

path = "/home/voldemort/GitHub/Login-Pages/login-form-08/login-form-08"
if not path.endswith("/"):
    path += "/"
def reverse(text):
    text = list(text)
    text.reverse()
    text = "".join(text)
    return text
def search(path):
    
        for file in os.listdir(path):
            pathandfile = os.path.join(path, file)
            if os.path.isfile(os.path.join(path, file)):
                os.system("chown voldemort " + pathandfile)
            else:
                os.system("chown voldemort " + pathandfile)
                search(pathandfile)
            print(pathandfile)
search(path)
