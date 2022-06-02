import yaml
import os


def executeCommand(varray):
    for v in varray:
        stream = os.popen(v)
        lines = stream.readlines()
        for line in lines:
            print(f"debut {line}")

with open('data.yml') as f:
    data = yaml.load_all(f, Loader=yaml.FullLoader)
    for doc in data:
        print(f" appName {doc['app']}")
        print(f" scheduler {doc['scheduler']}")
        print(
            f" os {doc['os']['image']}: {doc['os']['version']} - {doc['os']['lang']}")
        
        for k, varray in doc.items():
            
            if k == "command":
                executeCommand(varray)
        


