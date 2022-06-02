import os
from pathlib import Path


rootPath = f"C:/Users/asus/toto"
if(os.path.exists(rootPath) and os.path.isdir(rootPath)):
    os.chdir(rootPath)
    for el in os.listdir(rootPath):
        pEl = Path(el)
        print(f"{pEl.stem} : {pEl.__sizeof__()} du coup {pEl.suffix} ")
        print(pEl.absolute())
        print(Path(pEl.absolute()).as_uri())

'#path = rootPath + "/log"'
path = os.path.join(rootPath, "log")
logFile ="file.log"
if (os.path.exists(path) == False):
    os.mkdir(path)

path += os.path.join(path,logFile)

if (os.path.exists(path) == True):
    os.remove(path)


'''
for el in os.listdir(rootPath):
    pEl = Path(el)
    print(f"{pEl.stem} : {pEl.__sizeof__()} du coup {pEl.suffix} ")'''
    
for el in Path(rootPath).glob('**/*.txt'):
    pEl = Path(el)
    print(f"{pEl.stem} : {pEl.__sizeof__()} du coup {pEl.suffix} ")
