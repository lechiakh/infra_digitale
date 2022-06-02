import subprocess
#process = subprocess.Popen(['echo', 'More output'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
#stdout, stderr = process.communicate()
#stdout, stderr
with open('test.txt', 'w') as f: process = subprocess.Popen(['ls', '-l'], stdout=f)
