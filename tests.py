import os
from pathlib import Path
user = os.getlogin()
rootPath = f"C:/Users/{user}/toto"
if(os.path.exists(rootPath) and os.path.isdir(rootPath)):
    os.chdir(rootPath)
    for el in os.listdir(rootPath):
        pEl = Path(el)
        print(f"{pEl.stem} : {pEl.__sizeof__()} du coup {pEl.suffix} ")

path = rootPath + "/log"
logFile ="/file.log"
if (os.path.exists(path) == False):
    os.mkdir(path)

path += logFile

if (os.path.exists(path) == True):
    os.remove(path)

'os.mknod(path)'

for el in os.listdir(rootPath):
    pEl = Path(el)
    print(f"{pEl.stem} : {pEl.__sizeof__()} du coup {pEl.suffix} ")
