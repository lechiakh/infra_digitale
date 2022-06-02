from threading import * 
a = 1
def thread_1():
    global a
    print(a)
    a += 1

def thread_2():
    global a
    print(a)

first_thread = Thread(target = thread_1)
second_thread = Thread(target = thread_2)

first_thread.start()

second_thread.start()