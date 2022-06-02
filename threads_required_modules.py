# Import required modules
from threading import *
# Creating class
class Gfg:
# Creating instance method
 def method1(self):
  for i in range(6):
   print('Child Thread')
# Driver Code
# Creating object of Gfg class
obj = Gfg()
# Creating object of thread by
# targeting instance method of Gfg class
thread_obj = Thread(target=obj.method1)
# Call the target function of threa
thread_obj.start()
# for loop executed by main thread
for i in range(6):
 print('Main Thread')
