import os
stream = os.popen('dir -l')
lines = stream.readlines()
for line in lines:
    print(f"debut {line} fin")

