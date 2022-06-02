import os
#os.system('ls -l')
stream = os.popen('echo Returned output')
output = stream.read()
print(output)
