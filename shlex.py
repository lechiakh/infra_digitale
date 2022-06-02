import subprocess
import shlex
#query = shlex.split('ls -l')
query = ['ping','www.google.com']
with open('console.log', 'w') as f:
    process = subprocess.Popen(query,
                            stdout=f,
                            stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
