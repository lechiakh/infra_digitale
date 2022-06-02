import logging
import time
import threading
COMPTEUR = 0
def incr():
 global COMPTEUR
 for c in range(100000):
  v = COMPTEUR
  COMPTEUR = v + 1
th = []
for n in range(4):
 t = threading.Thread(target=incr, args=[])
 t.start()
 time.sleep(0.1)
 logging.info('Thread Started')
 th.append(t)
for t in th:
 t.join()
print("Valeur finale : {}".format(COMPTEUR))
